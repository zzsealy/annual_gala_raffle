"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import ky from "ky";

export default function ConfigPage() {
  const router = useRouter();
  
  const [prizeLevel, setPrizeLevel] = useState(3);
  const [personNum, setPersonNum] = useState(5);
  const [prizeType, setPrizeType] = useState("gift");
  const [insertPosition, setInsertPosition] = useState("after");
  const [isSubmitting, setIsSubmitting] = useState(false);

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
          person_num: personNum,
        },
      });
      alert("添加抽奖轮次成功！");
    } catch (error) {
      console.error(error);
      alert("添加失败，请查看控制台");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center relative">
      <div className="absolute top-6 left-6 text-gray-600 font-medium">
        提示：按下键盘上的 <kbd className="bg-gray-800 text-white px-2 py-1 rounded font-bold shadow-sm">G</kbd> 键返回抽奖页面
      </div>
      
      <div className="bg-white p-8 rounded-xl shadow-2xl w-[400px] border border-gray-200">
        <h1 className="text-2xl font-black text-gray-900 mb-6 border-b-2 border-gray-100 pb-3">⚙️ 抽奖配置管理</h1>
        
        <div className="flex flex-col gap-5">
          <div>
            <label className="block text-gray-900 font-bold mb-2 text-lg">奖项等级</label>
            <select 
              value={prizeLevel} 
              onChange={(e) => setPrizeLevel(Number(e.target.value))}
              className="w-full border-2 border-gray-300 rounded-lg p-3 text-gray-900 font-medium text-lg focus:outline-none focus:border-red-500 focus:ring-1 focus:ring-red-500"
            >
              <option value={0}>特等奖</option>
              <option value={1}>一等奖</option>
              <option value={2}>二等奖</option>
              <option value={3}>三等奖</option>
            </select>
          </div>

          <div>
            <label className="block text-gray-900 font-bold mb-2 text-lg">抽奖人数</label>
            <input 
              type="number" 
              min={1}
              value={personNum} 
              onChange={(e) => setPersonNum(Number(e.target.value))}
              className="w-full border-2 border-gray-300 rounded-lg p-3 text-gray-900 font-medium text-lg focus:outline-none focus:border-red-500 focus:ring-1 focus:ring-red-500"
            />
          </div>

          <div>
            <label className="block text-gray-900 font-bold mb-2 text-lg">奖品类型</label>
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

          <div>
            <label className="block text-gray-900 font-bold mb-2 text-lg">插入位置</label>
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
    </div>
  );
}
