"use client";

import { useEffect, useState, useRef } from "react";
import { useRouter } from "next/navigation";
import { motion, useAnimationFrame } from "framer-motion";
import ky from "ky";

interface WinnerRecord {
  name: string;
  code: string;
  desc: string;
}

export default function WinnersPage() {
  const router = useRouter();
  const [records, setRecords] = useState<WinnerRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const scrollRef = useRef<HTMLDivElement>(null);
  const [scrollY, setScrollY] = useState(0);

  useEffect(() => {
    const fetchRecords = async () => {
      try {
        const res: WinnerRecord[] = await ky
          .get(`${process.env.NEXT_PUBLIC_API_URL}/api/raffle_records`)
          .json();
        setRecords(res);
      } catch (err) {
        console.error("Failed to fetch records:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchRecords();

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Enter") {
        router.push("/");
      } else if (e.key.toLowerCase() === "g") {
        router.push("/config");
      } else if (e.key === " ") {
        router.push("/");
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [router]);

  const [isPaused, setIsPaused] = useState(false);
  const pauseStartTime = useRef<number>(0);

  // 自动滚动逻辑
  useAnimationFrame((time) => {
    if (loading || !scrollRef.current || records.length === 0) return;

    if (isPaused) {
      if (time - pauseStartTime.current > 3000) {
        setIsPaused(false);
        setScrollY(0);
      }
      return;
    }

    const speed = 0.8;
    setScrollY((prev) => {
      const next = prev + speed;
      const containerHeight =
        scrollRef.current?.parentElement?.clientHeight || 0;
      const contentHeight = scrollRef.current!.scrollHeight;

      // 当滚动到最后一行完全消失（或者只剩一点点空白）时停止
      // 我们在内容底部加了 padding，所以 contentHeight 会比较大
      if (next >= contentHeight - containerHeight + 100) {
        setIsPaused(true);
        pauseStartTime.current = time;
        return prev;
      }
      return next;
    });
  });

  if (loading) {
    return (
      <div className="w-screen h-screen bg-[#800101] flex items-center justify-center text-[#FFDBA6] text-2xl font-bold">
        正在加载中奖名单...
      </div>
    );
  }

  return (
    <div
      className="relative w-screen h-screen overflow-hidden bg-no-repeat bg-cover flex flex-col items-center"
      style={{
        backgroundImage: "url('/images/raffle/background.png')",
        backgroundSize: "100% 100%",
      }}
    >
      {/* 顶部标题 */}
      <div className="mt-12 mb-8 z-10">
        <h1
          className="text-5xl md:text-6xl font-extrabold text-[#FFE7B4] drop-shadow-[0_4px_8px_rgba(0,0,0,0.8)] tracking-[0.2em]"
          style={{
            WebkitTextStroke: "1px #DE1010",
            fontFamily:
              '"Microsoft YaHei", "PingFang SC", "Noto Sans SC", sans-serif',
          }}
        >
          中奖名单
        </h1>
      </div>

      {/* 名单容器 */}
      <div className="flex-1 w-[80%] max-w-5xl bg-black/30 backdrop-blur-md rounded-2xl border-2 border-[#FFE7B4]/30 overflow-hidden mb-12 shadow-2xl relative">
        {/* 表头 */}
        <div className="grid grid-cols-3 py-6 px-10 bg-[#DE1010]/80 text-[#FFE7B4] text-2xl font-bold border-b border-[#FFE7B4]/50 z-20 relative">
          <div className="text-center">工号</div>
          <div className="text-center">姓名</div>
          <div className="text-center">奖项</div>
        </div>

        <div className="relative h-[calc(100%-80px)] overflow-hidden">
          <motion.div
            ref={scrollRef}
            className="flex flex-col"
            style={{
              y: -scrollY,
              paddingBottom: "50vh", // 在底部留出大量空白
            }}
          >
            {records.map((item, index) => (
              <div
                key={index}
                className="grid grid-cols-3 py-6 px-10 text-white text-xl border-b border-white/10 hover:bg-white/5 transition-colors items-center"
              >
                <div className="text-center font-mono opacity-80">
                  {item.code}
                </div>
                <div className="text-center font-bold text-[#FFE7B4]">
                  {item.name}
                </div>
                <div className="text-center text-[#FFDBA6]">{item.desc}</div>
              </div>
            ))}

            {records.length === 0 && (
              <div className="flex items-center justify-center h-64 text-white/50 text-2xl">
                暂无中奖记录
              </div>
            )}

            {/* 结尾提示文字 */}
            {records.length > 0 && (
              <div className="py-20 text-center text-[#FFE7B4]/40 text-lg italic tracking-widest leading-loose"></div>
            )}
          </motion.div>
        </div>
      </div>

      {/* 底部提示 */}
      <div className="absolute bottom-4 right-8 text-[#FFE7B4]/60 text-sm">
        按 Enter 返回主页 | 按 G 进入配置
      </div>
    </div>
  );
}
