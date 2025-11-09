def main():
  import random  # 一定要放在最上面
import time

def cast_blocks():
    import random
    block1 = random.choice(['陽', '陰'])
    block2 = random.choice(['陽', '陰'])
    print(f"筊杯一號: {block1}")
    print(f"筊杯二號: {block2}")
    print("-" * 20)
    if block1 != block2:
        return "聖杯"
    elif block1 == '陽' and block2 == '陽':
        return "怒杯"
    else:
        return "哭杯"

def get_fortune():
    import random
    lucky_colors = ["紅色", "金色", "藍色", "綠色", "紫色", "橘色", "白色", "黑色"]
    lucky_directions = ["東方", "南方", "西方", "北方", "東南方", "西南方", "西北方", "東北方"]
    love_luck = random.randint(1, 5)
    career_luck = random.randint(1, 5)
    wealth_luck = random.randint(1, 5)
    love_stars = '★' * love_luck + '☆' * (5 - love_luck)
    career_stars = '★' * career_luck + '☆' * (5 - career_luck)
    wealth_stars = '★' * wealth_luck + '☆' * (5 - wealth_luck)
    print("\n🎉 恭喜！神明允許為您指點迷津 🎉")
    print("-" * 30)
    time.sleep(1)
    print(f"今日幸運色： {random.choice(lucky_colors)}")
    time.sleep(0.5)
    print(f"今日好運方位： {random.choice(lucky_directions)}")
    time.sleep(0.5)
    print("\n--- 運勢評分 ---")
    print(f"愛情運： {love_stars}")
    time.sleep(0.5)
    print(f"事業運： {career_stars}")
    time.sleep(0.5)
    print(f"財運： {wealth_stars}")
    print("-" * 30)

def main():
    import random
    print("=" * 30)
    print("     線上誠心擲筊算命")
    print("=" * 30)
    input("心中默念您的問題，然後按 Enter 鍵開始擲筊...")
    print("\n正在虔誠地擲出筊杯...")
    time.sleep(2)
    result = cast_blocks()
    print(f"擲筊結果: 【{result}】")
    print("-" * 20)
    time.sleep(1)
    if result == "聖杯":
        get_fortune()
    elif result == "怒杯":
        print("神明似乎不太同意，請稍後再試。")
    elif result == "哭杯":
        print("神明笑而不語，狀況不明，請您釐清問題後再試一次。")
    print("\n感謝您的使用，祝您有美好的一天！")

if __name__ == "__main__":
    main()

   