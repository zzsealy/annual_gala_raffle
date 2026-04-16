"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import ky from "ky";

interface QueueItem {
  id: number;
  desc: string;
  raffleQueuePersonNum: number;
}

const SPECIAL_PRIZE_LEVEL = -1;

export default function ConfigPage() {
  const router = useRouter();

  const [prizeLevel, setPrizeLevel] = useState(3);
  const [personNum, setPersonNum] = useState(5);
  const [prizeType, setPrizeType] = useState("gift");
  const [specialPosition, setSpecialPosition] = useState("左");
  const [insertPosition, setInsertPosition] = useState("after");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [queues, setQueues] = useState<QueueItem[]>([]);

  const isSpecialPrize = prizeLevel === SPECIAL_PRIZE_LEVEL;

  const fetchQueues = async () => {
    try {
      const res: QueueItem[] = await ky
        .get(`${process.env.NEXT_PUBLIC_API_URL}/api/raffle_queue`)
        .json();
      setQueues(res);
    } catch (e) {
      console.error(e);
    }
  };

  useEffect(() => {
    fetchQueues();
  }, []);

  useEffect(() => {
    if (isSpecialPrize) {
      setPersonNum(1);
    }
  }, [isSpecialPrize]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key.toLowerCase() === "g") {
        router.push("/");
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [router]);

  const handleAddQueue = async () => {
    if (isSubmitting) return;
    setIsSubmitting(true);
    try {
      await ky.post(`${process.env.NEXT_PUBLIC_API_URL}/api/raffle_queue/add`, {
        json: {
          prize_level: prizeLevel,
          prize_type: prizeType,
          insert_position: insertPosition,
          person_num: isSpecialPrize ? 1 : personNum,
          special_position: isSpecialPrize ? specialPosition : null,
        },
      });
      alert("添加抽奖轮次成功！");
      fetchQueues(); // 重新拉取队列数据
    } catch (error) {
      console.error(error);
      alert("添加失败，请查看控制台");
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleReset = async () => {
    if (
      !window.confirm(
        "❗ 警告：这将清空所有已有中奖记录，重置所有已中奖人的状态，并将抽奖队列恢复为初始状态！\n\n确定要重置吗？",
      )
    )
      return;

    try {
      if (isSubmitting) return;
      setIsSubmitting(true);
      await ky.post(
        `${process.env.NEXT_PUBLIC_API_URL}/api/raffle_queue/reset`,
      );
      alert("重置成功！所有数据已被清空。");
      fetchQueues();
    } catch (e) {
      console.error(e);
      alert("重置失败，见控制台。");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center relative">
      <div className="absolute top-6 left-6 text-gray-600 font-medium">
        提示：按下键盘上的{" "}
        <kbd className="bg-gray-800 text-white px-2 py-1 rounded font-bold shadow-sm">
          G
        </kbd>{" "}
        键返回抽奖页面
      </div>

      <div className="flex gap-8 items-stretch pt-12">
        {/* 左侧：抽奖配置表单 */}
        <div className="bg-white p-8 rounded-xl shadow-2xl w-[400px] border border-gray-200 flex flex-col h-[700px]">
          <h1 className="text-2xl font-black text-gray-900 mb-6 border-b-2 border-gray-100 pb-3">
            ⚙️ 抽奖配置管理
          </h1>

          <div className="flex flex-col gap-5">
            <div>
              <label className="block text-gray-900 font-bold mb-2 text-lg">
                奖项等级
              </label>
              <select
                value={prizeLevel}
                onChange={(e) => setPrizeLevel(Number(e.target.value))}
                className="w-full border-2 border-gray-300 rounded-lg p-3 text-gray-900 font-medium text-lg focus:outline-none focus:border-red-500 focus:ring-1 focus:ring-red-500"
              >
                <option value={SPECIAL_PRIZE_LEVEL}>特别大奖</option>
                <option value={0}>特等奖</option>
                <option value={1}>一等奖</option>
                <option value={2}>二等奖</option>
                <option value={3}>三等奖</option>
              </select>
            </div>

            <div>
              <label className="block text-gray-900 font-bold mb-2 text-lg">
                抽奖人数
              </label>
              <input
                type="number"
                min={1}
                value={personNum}
                onChange={(e) => setPersonNum(Number(e.target.value))}
                disabled={isSpecialPrize}
                className="w-full border-2 border-gray-300 rounded-lg p-3 text-gray-900 font-medium text-lg focus:outline-none focus:border-red-500 focus:ring-1 focus:ring-red-500"
              />
              {isSpecialPrize && (
                <p className="mt-2 text-sm text-gray-500">
                  特别大奖固定只抽 1 人，展示效果与特等奖一致。
                </p>
              )}
            </div>

            {isSpecialPrize ? (
              <div>
                <label className="block text-gray-900 font-bold mb-2 text-lg">
                  左右半场
                </label>
                <div className="flex gap-6">
                  <label className="flex items-center gap-2 cursor-pointer text-gray-900 font-medium text-lg">
                    <input
                      type="radio"
                      name="specialPosition"
                      value="左"
                      checked={specialPosition === "左"}
                      onChange={(e) => setSpecialPosition(e.target.value)}
                      className="w-5 h-5 text-red-600 focus:ring-red-500"
                    />
                    左半场
                  </label>
                  <label className="flex items-center gap-2 cursor-pointer text-gray-900 font-medium text-lg">
                    <input
                      type="radio"
                      name="specialPosition"
                      value="右"
                      checked={specialPosition === "右"}
                      onChange={(e) => setSpecialPosition(e.target.value)}
                      className="w-5 h-5 text-red-600 focus:ring-red-500"
                    />
                    右半场
                  </label>
                </div>
              </div>
            ) : (
              <div>
                <label className="block text-gray-900 font-bold mb-2 text-lg">
                  奖品类型
                </label>
                <div className="flex gap-6">
                  <label className="flex items-center gap-2 cursor-pointer text-gray-900 font-medium text-lg">
                    <input
                      type="radio"
                      name="prizeType"
                      value="gift"
                      checked={prizeType === "gift"}
                      onChange={(e) => setPrizeType(e.target.value)}
                      className="w-5 h-5 text-red-600 focus:ring-red-500"
                    />
                    实物
                  </label>
                  <label className="flex items-center gap-2 cursor-pointer text-gray-900 font-medium text-lg">
                    <input
                      type="radio"
                      name="prizeType"
                      value="cash"
                      checked={prizeType === "cash"}
                      onChange={(e) => setPrizeType(e.target.value)}
                      className="w-5 h-5 text-red-600 focus:ring-red-500"
                    />
                    现金
                  </label>
                </div>
              </div>
            )}

            <div>
              <label className="block text-gray-900 font-bold mb-2 text-lg">
                插入位置
              </label>
              <div className="flex gap-6">
                <label className="flex items-center gap-2 cursor-pointer text-gray-900 font-medium text-lg">
                  <input
                    type="radio"
                    name="insertPosition"
                    value="before"
                    checked={insertPosition === "before"}
                    onChange={(e) => setInsertPosition(e.target.value)}
                    className="w-5 h-5 text-red-600 focus:ring-red-500"
                  />
                  插入队列前
                </label>
                <label className="flex items-center gap-2 cursor-pointer text-gray-900 font-medium text-lg">
                  <input
                    type="radio"
                    name="insertPosition"
                    value="after"
                    checked={insertPosition === "after"}
                    onChange={(e) => setInsertPosition(e.target.value)}
                    className="w-5 h-5 text-red-600 focus:ring-red-500"
                  />
                  插入队列后
                </label>
              </div>
            </div>

            <button
              onClick={handleAddQueue}
              disabled={isSubmitting}
              className="mt-6 w-full bg-red-600 hover:bg-red-700 text-white font-black text-lg py-4 rounded-lg shadow border-2 border-red-700 transition-colors disabled:bg-gray-400 disabled:border-gray-500"
            >
              {isSubmitting ? "添加中..." : "➕ 新增抽奖轮次"}
            </button>
          </div>
        </div>

        {/* 右侧：当前抽奖队列列表 */}
        <div className="bg-white p-8 rounded-xl shadow-2xl w-[450px] border border-gray-200 flex flex-col h-[700px]">
          <h1 className="text-2xl font-black text-gray-900 mb-6 border-b-2 border-gray-100 pb-3">
            📜 实时抽奖队列
          </h1>

          {queues.length === 0 ? (
            <div className="flex flex-col items-center justify-center flex-1 text-gray-400 font-medium">
              <span className="text-4xl mb-3">📭</span>
              <span>当前没有尚未抽奖的轮次哦~</span>
            </div>
          ) : (
            <div className="flex flex-col gap-4 overflow-y-auto pr-2 custom-scrollbar">
              {queues.map((q, index) => (
                <div
                  key={q.id}
                  className="p-5 border border-gray-200 rounded-xl flex justify-between items-center shadow-sm hover:shadow-md transition-shadow bg-gray-50"
                >
                  <div className="flex flex-col gap-1">
                    <div className="text-xl font-bold text-gray-800">
                      {q.desc}
                    </div>
                    <div className="text-sm text-gray-500 font-medium">
                      抽取人数:{" "}
                      <span className="text-red-600 font-bold">
                        {q.raffleQueuePersonNum}
                      </span>{" "}
                      人
                    </div>
                  </div>
                  <div className="flex flex-col items-end gap-2">
                    <div className="bg-red-100 border border-red-200 text-red-800 text-xs font-bold px-3 py-1 rounded-full shadow-sm">
                      第 {index + 1} 场
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}

          <div className="mt-6 pt-6 border-t font-semibold border-gray-100 text-center">
            <button
              onClick={handleReset}
              disabled={isSubmitting}
              className="w-full bg-gray-800 hover:bg-gray-900 text-white font-bold py-3 rounded-lg shadow border border-gray-700 transition-colors disabled:bg-gray-400"
            >
              {isSubmitting ? "正在执行..." : "⚠️ 一键重置所有抽奖数据"}
            </button>
            <p className="text-xs text-gray-500 mt-3 font-normal">
              点击将清空记录、还原中奖名单并重置队列
            </p>
          </div>
        </div>
      </div>

      <style
        dangerouslySetInnerHTML={{
          __html: `
        .custom-scrollbar::-webkit-scrollbar {
          width: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: #f1f1f1;
          border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: #d4d4d4;
          border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: #a8a8a8;
        }
      `,
        }}
      />
    </div>
  );
}
