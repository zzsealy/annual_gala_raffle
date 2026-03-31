"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import ky from "ky";
import RafflePage from "@/components/raffle_page";

export default function IndexPage() {
  const router = useRouter();
  const [raffle_level, setRaffleLevel] = useState(3);
  const [raffleQueuePersonNum, setRaffleQueuePersonNum] = useState(0);
  const [imageUrl, setImageUrl] = useState("");
  const [persons, setPersons] = useState([]);
  const [queueId, setQueueId] = useState(0); // 抽奖队列的id
  const [canRaffle, setCanRaffle] = useState(true);
  const [raffle_level_desc, setRaffleLevelDesc] = useState("");

  const fetch_raffle_queue = async () => {
    const res: any[] = await ky
      .get(`${process.env.NEXT_PUBLIC_API_URL}/api/raffle_queue`)
      .json();
    if (res.length === 0) {
      setCanRaffle(false);
      return;
    }
    console.log(res);
    setCanRaffle(true); // 如果添加了新的抽奖队列对象，需要重置此状态
    setRaffleLevel(res[0].prize_level);
    setRaffleQueuePersonNum(res[0].raffleQueuePersonNum);
    setImageUrl(res[0].img_url);
    setQueueId(res[0].id);
    setRaffleLevelDesc(res[0].desc);
  };

  const fetch_persons = async () => {
    const res: any = await ky
      .get(`${process.env.NEXT_PUBLIC_API_URL}/api/persons`)
      .json();
    setPersons(res);
  };

  useEffect(() => {
    // 每次进入主页都会触发这段代码，可以在这里写正式的 axios/fetch 接口请求
    console.log("主页加载完毕，正在请求接口...");
    // 模拟请求的写法：
    // fetch("/api/xxx").then(res => res.json()).then(data => console.log(data));

    const handleKeyDown = (e: KeyboardEvent) => {
      // 监听回车键，跳转到抽奖主页
      if (e.key === "Enter") {
        router.push("/raffle_home");
      } else if (e.key.toLowerCase() === "g") {
        router.push("/config");
      } else if (e.key === " ") {
        router.push("/winners");
      }
    };

    // 挂载键盘监听事件
    window.addEventListener("keydown", handleKeyDown);

    // 触发网络请求
    fetch_raffle_queue();
    fetch_persons();

    // 清理事件监听，防止内存泄漏和多次绑定
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [router]);

  return (
    <div className="w-screen h-screen flex flex-col items-center justify-center bg-gray-50 text-gray-800">
      <RafflePage
        raffle_level={raffle_level}
        raffleQueuePersonNum={raffleQueuePersonNum}
        imageUrl={imageUrl}
        persons={persons}
        queueId={queueId}
        canRaffle={canRaffle}
        raffle_level_desc={raffle_level_desc}
        onClose={() => {
          fetch_raffle_queue();
          fetch_persons();
        }}
      />
    </div>
  );
}
