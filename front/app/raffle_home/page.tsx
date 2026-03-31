"use client";

import { motion } from "framer-motion";
import { useEffect } from "react";
import { useRouter } from "next/navigation";

export default function rafflePage() {
  const router = useRouter();

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // 监听回车键返回主页
      if (e.key === "Enter") {
        router.push("/");
      } else if (e.key.toLowerCase() === "g") {
        router.push("/config");
      } else if (e.key === " ") {
        router.push("/winners");
      }
    };
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [router]);

  // 定义烟花的爆炸循环动画（从0变大，然后透明消失）
  const fireworkVariants = (delay: number) => ({
    animate: {
      scale: [0, 1.2, 1.5],
      opacity: [1, 1, 0],
      transition: {
        duration: 2.5,
        repeat: Infinity,
        ease: "easeOut" as const,
        delay: delay,
        times: [0, 0.4, 1], // 控制动画的时间节点，0.4的时候缩放最大
      },
    },
  });

  // 定义元素的浮动/抖动动画（上下浮动，带一点轻轻的旋转）
  const floatVariants = (delay: number) => ({
    animate: {
      y: [-15, 15, -15],
      rotate: [-3, 3, -3],
      transition: {
        duration: 4,
        repeat: Infinity,
        ease: "easeInOut" as const,
        delay: delay,
      },
    },
  });

  // 定义主标题“幸运抽奖”的缓动呼吸/抖动效果
  const titleVariants = {
    animate: {
      scale: [1, 1.03, 1],
      y: [-8, 8, -8],
      rotate: [-1, 1, -1],
      transition: {
        duration: 3,
        repeat: Infinity,
        ease: "easeInOut" as const,
      },
    },
  };

  return (
    <div
      className="relative w-screen h-screen overflow-hidden bg-cover bg-center bg-no-repeat"
      style={{ backgroundImage: "url('/images/home/background.png')" }}
    >
      {/* ======================= 烟花组 ======================= */}
      {/* 左上脚的烟花 */}
      <motion.img
        src="/images/home/fireworks_left.png"
        alt="firework left"
        className="absolute top-[8%] left-[6%] w-[18vw] opacity-0"
        variants={fireworkVariants(0)}
        animate="animate"
      />
      {/* 右上角偏内的烟花 */}
      <motion.img
        src="/images/home/fireworks_middle.png"
        alt="firework middle"
        className="absolute top-[12%] right-[22%] w-[15vw] opacity-0"
        variants={fireworkVariants(0.8)}
        animate="animate"
      />
      {/* 右上角最边上的烟花 */}
      <motion.img
        src="/images/home/fireworks_right.png"
        alt="firework right"
        className="absolute top-[4%] right-[2%] w-[20vw] opacity-0"
        variants={fireworkVariants(1.5)}
        animate="animate"
      />

      {/* ==================== 浮动的恭喜发财 ==================== */}
      {/* 恭 - 左上区域 */}
      <motion.img
        src="/images/home/恭.png"
        alt="恭"
        className="absolute top-[15%] left-[18%] w-[10vw] z-10"
        variants={floatVariants(0)}
        animate="animate"
      />
      {/* 喜 - 右下 */}
      <motion.img
        src="/images/home/喜.png"
        alt="喜"
        className="absolute bottom-[28%] left-[15%] w-[10vw] z-10"
        variants={floatVariants(0.7)}
        animate="animate"
      />
      {/* 发 - 左下靠近中间 */}
      <motion.img
        src="/images/home/发.png"
        alt="发"
        className="absolute bottom-[2%] left-[28%] w-[12vw] z-10"
        variants={floatVariants(1.2)}
        animate="animate"
      />
      {/* 财 - 左下最边缘 */}
      <motion.img
        src="/images/home/财.png"
        alt="财"
        className="absolute bottom-[18%] left-[8%] w-[9vw] z-10"
        variants={floatVariants(1.8)}
        animate="animate"
      />

      {/* ===================== 主标题：幸运抽奖 =================== */}
      {/* 绝对居中定位包裹器，使用百分比(vh)调整高度保证在4K/2K下偏移比例一致 */}
      <div
        className="absolute left-0 right-0 z-20 pointer-events-none flex justify-center"
        style={{ top: "0vh" }}
      >
        <motion.img
          src="/images/home/幸运抽奖.png"
          alt="幸运抽奖"
          className="w-[60vw]"
          variants={titleVariants}
          animate="animate"
        />
      </div>
    </div>
  );
}
