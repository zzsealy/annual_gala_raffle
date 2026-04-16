"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import ky from "ky";
import RafflePage from "@/components/raffle_page";

interface QueueItem {
  id: number;
  prize_level: number;
  raffleQueuePersonNum: number;
  img_url: string;
  desc: string;
}

interface PersonItem {
  code: string;
  name: string;
}

export default function IndexPage() {
  const router = useRouter();
  const [raffle_level, setRaffleLevel] = useState(3);
  const [raffleQueuePersonNum, setRaffleQueuePersonNum] = useState(0);
  const [imageUrl, setImageUrl] = useState("");
  const [persons, setPersons] = useState<PersonItem[]>([]);
  const [queueId, setQueueId] = useState(0); // 抽奖队列的id
  const [canRaffle, setCanRaffle] = useState(true);
  const [raffle_level_desc, setRaffleLevelDesc] = useState("");

  const fetch_persons = async (nextQueueId: number) => {
    const res: PersonItem[] = await ky
      .get(`${process.env.NEXT_PUBLIC_API_URL}/api/persons`, {
        searchParams: {
          queue_id: nextQueueId,
        },
      })
      .json();
    setPersons(res);
  };

  const fetchCurrentQueue = async () => {
    const res: QueueItem[] = await ky
      .get(`${process.env.NEXT_PUBLIC_API_URL}/api/raffle_queue`)
      .json();

    if (res.length === 0) {
      setCanRaffle(false);
      setPersons([]);
      setQueueId(0);
      setRaffleQueuePersonNum(0);
      setRaffleLevelDesc("");
      return;
    }

    const currentQueue = res[0];
    console.log(res);
    setCanRaffle(true); // 如果添加了新的抽奖队列对象，需要重置此状态
    setRaffleLevel(currentQueue.prize_level);
    setRaffleQueuePersonNum(currentQueue.raffleQueuePersonNum);
    setImageUrl(currentQueue.img_url);
    setQueueId(currentQueue.id);
    setRaffleLevelDesc(currentQueue.desc);
    await fetch_persons(currentQueue.id);
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
    fetchCurrentQueue();

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
          fetchCurrentQueue();
        }}
      />
    </div>
  );
}
