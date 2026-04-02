"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import confetti from "canvas-confetti";
import ky from "ky";

export default function RafflePage({
  raffle_level,
  raffleQueuePersonNum,
  imageUrl,
  persons,
  queueId,
  canRaffle,
  raffle_level_desc,
  onClose,
}: {
  raffle_level: number;
  raffleQueuePersonNum: number;
  imageUrl: string;
  persons: any[];
  queueId: number;
  canRaffle: boolean;
  raffle_level_desc: string;
  onClose?: () => void;
}) {
  // 状态管理
  const [isRolling, setIsRolling] = useState(false);
  const [isDrawn, setIsDrawn] = useState(false);
  const [winners, setWinners] = useState<{ code: string; name: string }[]>([]);

  // 基于真实传入的人员数据用于背景滚动
  const generateMockBlocks = () => {
    if (!persons || persons.length === 0) return [];

    const count = 40;
    const result: any[] = [];
    let lastCode = "";

    for (let i = 0; i < count; i++) {
      let p;
      // 尝试寻找一个跟上一个不一样的人
      // 增加尝试次数防止死循环（虽然在多人的情况下不会发生）
      let attempts = 0;
      do {
        p = persons[Math.floor(Math.random() * persons.length)];
        attempts++;
      } while (persons.length > 1 && p.code === lastCode && attempts < 10);

      // 特殊处理：如果是最后一个元素，还要确保它不等于第一个元素，防止无缝滚动时衔接处重复
      if (i === count - 1 && persons.length > 1 && p.code === result[0].code) {
        // 如果撞车了，再随机换一个，直到不撞第一个（简单处理）
        p =
          persons.find(
            (pp) => pp.code !== result[0].code && pp.code !== lastCode,
          ) || p;
      }

      result.push({
        code: p.code,
        name: p.name,
      });
      lastCode = p.code;
    }
    return result;
  };
  const [bgTracks, setBgTracks] = useState<any[][]>([[], [], [], []]);

  useEffect(() => {
    if (persons && persons.length > 0) {
      setBgTracks([
        generateMockBlocks(),
        generateMockBlocks(),
        generateMockBlocks(),
        generateMockBlocks(),
      ]);
    }
  }, [persons]);

  // 触发强化版礼花动画
  const fireCorners = () => {
    // 1. 左下角巨大爆发
    confetti({
      particleCount: 200,
      angle: 60,
      spread: 100,
      origin: { x: 0, y: 1 },
      startVelocity: 70,
      scalar: 1.5, // 纸屑放大 1.5 倍
      zIndex: 100,
    });

    // 2. 右下角巨大爆发
    confetti({
      particleCount: 200,
      angle: 120,
      spread: 100,
      origin: { x: 1, y: 1 },
      startVelocity: 70,
      scalar: 1.5,
      zIndex: 100,
    });

    // 3. 半秒后在中间下起金红大爆竹雨
    setTimeout(() => {
      confetti({
        particleCount: 250,
        spread: 180,
        origin: { y: 0.6 },
        startVelocity: 50,
        scalar: 1.8, // 纸屑放大 1.8 倍
        zIndex: 100,
        colors: ["#FFE7B4", "#DE1010", "#FFFFFF", "#FFD700", "#FF4500"],
      });
    }, 400);
  };

  const fetch_winners = async () => {
    const res: any[] = await ky
      .post(`${process.env.NEXT_PUBLIC_API_URL}/api/raffle`, {
        json: {
          queue_id: queueId,
        },
      })
      .json();
    setWinners(res);
  };

  // 点击抽奖事件
  const handleStartDraw = async () => {
    if (isRolling || isDrawn || !canRaffle) return;

    setIsRolling(true);
    await fetch_winners();

    // TODO: 这里是真正调用后端抽取获奖名单的接口，现在我们用真实传入的人员名单打乱做临时模拟
    // 滚动 5 秒钟
    await new Promise((resolve) => setTimeout(resolve, 5000));

    // 拿到结果，停止滚动，弹出中奖框
    setIsRolling(false);
    setIsDrawn(true);
    fireCorners(); // 放礼花！
  };

  const winnerCount = winners.length || raffleQueuePersonNum;

  const getWinnerLayout = (level: number, count: number) => {
    const safeCount = Math.max(count, 1);

    if (level === 0) {
      if (safeCount === 1) {
        return {
          containerClass: "w-[clamp(220px,20vw,320px)]",
          columns: 1,
          cardAspectRatio: "1.05 / 1",
          codeFontSize: "clamp(28px, 2.2vw, 40px)",
          nameFontSize: "clamp(24px, 1.8vw, 34px)",
        };
      }

      if (safeCount === 2) {
        return {
          containerClass: "w-[min(52vw,720px)]",
          columns: 2,
          cardAspectRatio: "1.15 / 1",
          codeFontSize: "clamp(24px, 2vw, 34px)",
          nameFontSize: "clamp(20px, 1.6vw, 28px)",
        };
      }

      if (safeCount <= 4) {
        return {
          containerClass: "w-[min(58vw,820px)]",
          columns: 2,
          cardAspectRatio: "1.25 / 1",
          codeFontSize: "clamp(22px, 1.8vw, 30px)",
          nameFontSize: "clamp(18px, 1.4vw, 24px)",
        };
      }

      if (safeCount <= 6) {
        return {
          containerClass: "w-[min(72vw,980px)]",
          columns: 3,
          cardAspectRatio: "1.35 / 1",
          codeFontSize: "clamp(20px, 1.6vw, 28px)",
          nameFontSize: "clamp(17px, 1.25vw, 22px)",
        };
      }

      return {
        containerClass: "w-[min(82vw,1180px)]",
        columns: Math.min(4, safeCount),
        cardAspectRatio: "1.45 / 1",
        codeFontSize: "clamp(18px, 1.45vw, 24px)",
        nameFontSize: "clamp(16px, 1.1vw, 20px)",
      };
    }

    return {
      containerClass:
        safeCount === 1 ? "w-[clamp(240px,24vw,360px)]" : "w-[80%] max-w-6xl",
      columns:
        safeCount >= 5 ? 5 : safeCount === 3 ? 3 : safeCount === 2 ? 2 : 1,
      cardAspectRatio: safeCount === 1 ? "1.2 / 1" : "2 / 1",
      codeFontSize:
        safeCount === 1 ? "clamp(26px, 2.2vw, 38px)" : "clamp(20px, 2vw, 32px)",
      nameFontSize:
        safeCount === 1
          ? "clamp(22px, 1.8vw, 32px)"
          : "clamp(18px, 1.6vw, 26px)",
    };
  };

  const winnerLayout = getWinnerLayout(raffle_level, winnerCount);

  // 获取奖项名称
  const getPrizeName = (level: number) => {
    if (level === 0) return "特等奖";
    if (level === 1) return "一等奖";
    if (level === 2) return "二等奖";
    if (level === 3) return "三等奖";
    return `${level}等奖`;
  };

  return (
    <div
      className="relative w-screen h-screen overflow-hidden bg-no-repeat"
      style={{
        backgroundImage: "url('/images/raffle/background.png')",
        backgroundSize: "102% 102%",
        backgroundPosition: "-2vw center",
      }}
    >
      {/* 纯 CSS 动画统一定义区 */}
      <style
        dangerouslySetInnerHTML={{
          __html: `
        @keyframes scrollLeft {
          0% { transform: translateX(0); }
          100% { transform: translateX(-50%); }
        }
        @keyframes scrollRight {
          0% { transform: translateX(-50%); }
          100% { transform: translateX(0); }
        }
        .animate-scroll-left {
          animation: scrollLeft 40s linear infinite;
        }
        .animate-scroll-right {
          animation: scrollRight 40s linear infinite;
        }
        /* 抽奖时加速动画 */
        .rolling-fast .animate-scroll-left {
          animation: scrollLeft 1.5s linear infinite;
        }
        .rolling-fast .animate-scroll-right {
          animation: scrollRight 1.5s linear infinite;
        }
      `,
        }}
      />

      {/* 顶部标题 */}
      <div className="absolute top-6 left-0 right-0 z-10 flex justify-center pointer-events-none">
        <h1
          className="text-4xl md:text-5xl lg:text-6xl font-extrabold text-[#FFE7B4] drop-shadow-[0_4px_8px_rgba(200,0,0,0.8)]"
          style={{
            WebkitTextStroke: "1px #DE1010",
            letterSpacing: "8px",
            fontFamily:
              '"Microsoft YaHei", "PingFang SC", "Noto Sans SC", "SimHei", sans-serif',
          }}
        >
          普析35周年盛典暨第十五届职工代表大会抽奖活动
        </h1>
      </div>

      {/* ===================== 四行名字传送带 ===================== */}
      <div
        className={`absolute top-[18vh] left-0 right-0 z-0 flex flex-col gap-4 md:gap-8 ${isRolling ? "rolling-fast" : ""}`}
      >
        {bgTracks.map((track, trackIndex) => {
          // 单数行向左，双数行向右
          const isOdd = trackIndex % 2 === 0;
          const animationClass = isOdd
            ? "animate-scroll-left"
            : "animate-scroll-right";

          return (
            <div
              key={trackIndex}
              className="w-full overflow-hidden whitespace-nowrap opacity-90 relative"
            >
              <div
                className={`inline-flex gap-4 md:gap-8 w-max ${animationClass}`}
              >
                {/* 拼凑两份相同的数据实现无缝滚动 */}
                {[...track, ...track].map((item, i) => (
                  <div
                    key={i}
                    className="flex flex-col items-center justify-center rounded-md md:rounded-xl shadow-lg border-[1px] border-[#FFA0A0]"
                    style={{
                      // 背景渐变：#800101 -> #B61A1A
                      background:
                        "linear-gradient(135deg, #800101 0%, #B61A1A 100%)",
                      width: "12vw",
                      height: "7vw",
                    }}
                  >
                    <span className="text-[#FFDBA6] font-bold text-[1.8vw] leading-tight">
                      {item.code}
                    </span>
                    <span className="text-white font-medium text-[1.4vw]">
                      {item.name}
                    </span>
                  </div>
                ))}
              </div>
            </div>
          );
        })}
      </div>

      {/* ===================== 底部抽奖按钮 ===================== */}
      {!isDrawn && (
        <div className="absolute bottom-[8vh] left-0 right-0 flex justify-center z-20">
          <motion.button
            whileHover={canRaffle ? { scale: 1.05 } : {}}
            whileTap={canRaffle ? { scale: 0.95 } : {}}
            onClick={handleStartDraw}
            disabled={isRolling || !canRaffle}
            className={`rounded-full shadow-[0_8px_20px_rgba(200,0,0,0.5)] border-2 font-bold text-white tracking-widest flex items-center justify-center ${
              !canRaffle
                ? "cursor-not-allowed grayscale-[0.6] opacity-70 border-gray-400"
                : "cursor-pointer border-[#FFE8A1]"
            }`}
            style={{
              // 按钮渐变：#FFBA00 -> #FF7902 (正常) 或 灰色系 (禁用)
              background: canRaffle
                ? "linear-gradient(180deg, #FFBA00 0%, #FF7902 100%)"
                : "linear-gradient(180deg, #999 0%, #666 100%)",
              width: "25vw",
              height: "7vh",
              fontSize: "2.5vw",
              textShadow: "1px 1px 2px rgba(0,0,0,0.3)",
            }}
          >
            {isRolling ? "正在抽奖..." : !canRaffle ? "抽奖已结束" : "开始抽奖"}
          </motion.button>
        </div>
      )}

      {/* ===================== 中奖半透明遮罩与弹窗 ===================== */}
      <AnimatePresence>
        {isDrawn && (
          <motion.div
            className="absolute inset-0 z-50 flex flex-col items-center justify-center bg-black/60 backdrop-blur-sm"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
          >
            {/* 顶部的奖品信息区 */}
            <motion.div
              className="flex items-center gap-8 mb-12"
              initial={{ y: -50, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ delay: 0.2, type: "spring", stiffness: 200 }}
            >
              {/* 左侧：奖品图片展示区 (无论是否有图片路径都预留完美的红底边框位置) */}
              <div
                className={`${raffle_level === 0 ? "w-[10vw] h-[10vw]" : "w-[12vw] h-[12vw]"} bg-[#750A0A] border-[3px] border-[#FFF6D8] rounded-lg flex items-center justify-center p-2 shadow-2xl relative transition-all`}
              >
                {imageUrl ? (
                  /* eslint-disable-next-line @next/next/no-img-element */
                  <img
                    src={`/images${imageUrl}`}
                    alt="Prize"
                    // --- 你可以在这里调整图片大小 ---
                    // raffle_level === 0 代表特等奖。现在的设置是：特等奖占 65%，其他奖项占 85%
                    className={`${raffle_level === 0 ? "max-w-[65%] max-h-[65%]" : "max-w-[85%] max-h-[85%]"} object-contain`}
                  />
                ) : (
                  <span className="text-white/50 text-[1.5vw] font-bold">
                    [图片]
                  </span>
                )}
              </div>
              {/* 右侧：奖项级别 & 奖项描述（按照图示左对齐排列） */}
              <div className="flex flex-col text-left drop-shadow-md gap-2">
                <h2
                  className="text-[4vw] font-bold text-[#FFF6D8] tracking-widest leading-none"
                  style={{ textShadow: "2px 2px 4px rgba(0,0,0,0.5)" }}
                >
                  {getPrizeName(raffle_level)}
                </h2>
                {/* TODO: 这里留给你填入接口传回来的 desc，目前放个占位符 */}
                <p
                  className="text-[3vw] tracking-wider text-white font-bold"
                  style={{ textShadow: "1px 1px 3px rgba(0,0,0,0.5)" }}
                >
                  {/* 例如这里可以用 {prize_desc || "现金200元"} */}
                  {raffle_level_desc}
                </p>
              </div>
            </motion.div>

            {/* 下方的中奖名单展示区 */}
            <motion.div
              className={`grid gap-4 md:gap-6 ${winnerLayout.containerClass}`}
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              transition={{
                delay: 0.4,
                type: "spring",
                stiffness: 300,
                damping: 25,
              }}
              style={{
                gridTemplateColumns: `repeat(${winnerLayout.columns}, minmax(0, 1fr))`,
              }}
            >
              {winners.map((winner, idx) => (
                <motion.div
                  key={idx}
                  initial={{ scale: 0 }}
                  animate={{ scale: 1 }}
                  transition={{ delay: 0.5 + idx * 0.1, type: "spring" }} // 中奖卡片依次蹦出来
                  className="flex flex-col items-center justify-center rounded-lg shadow-2xl border-2 border-[#FFF0CB]"
                  style={{
                    // 中奖名单卡片使用了你提供的浅黄/橘黄效果
                    background:
                      "linear-gradient(180deg, #FFF6D8 0%, #FFD375 100%)",
                    aspectRatio: winnerLayout.cardAspectRatio,
                  }}
                >
                  <span
                    className="text-[#960000] font-bold leading-tight mb-1"
                    style={{ fontSize: winnerLayout.codeFontSize }}
                  >
                    {winner.code}
                  </span>
                  <span
                    className="text-[#B51E1E] font-medium"
                    style={{ fontSize: winnerLayout.nameFontSize }}
                  >
                    {winner.name}
                  </span>
                </motion.div>
              ))}
            </motion.div>

            {/* 点击空白处重新恢复组件状态(可选，如果需要点遮罩关闭) */}
            <div
              className="absolute top-4 right-8 text-white/50 cursor-pointer text-xl hover:text-white"
              onClick={() => {
                setIsDrawn(false);
                setWinners([]);
                if (onClose) onClose();
              }}
            >
              [关闭]
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
