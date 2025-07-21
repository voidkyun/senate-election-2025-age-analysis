

# 政党データ
# 政党キー: 政党名
parties={
	"jimin": "自民党",
	"komei": "公明党",
	"rikken": "立憲民主党",
	"ishin": "日本維新の会",
	"kokumin": "国国民民主党",
	"reiwa": "れいわ新選組",
	"kyosan": "日本共産党",
	"sansei": "参政党",
	"hoshu": "日本保守党",
	"shamin": "社会民主党",
	"nhk": "NHK党",
	"saisei": "再生の道",
	"mirai": "チーム未来",
	"kaikaku": "日本改革党",
	"seishin": "日本誠真会",
	"mushozoku": "無所属連合",
}

# 政党ごとの色設定
party_colors = {
	"jimin": "#AD1A1A",
	"komei": "#DF7D7A",
	"rikken": "#1966A5",
	"ishin": "#008E94",
	"kokumin": "#EFB21B",
	"reiwa": "#6D5BBC",
	"kyosan": "#41A2D8",
	"sansei": "#802058",
	"hoshu": "#41646D",
	"shamin": "#353573",
	"nhk": "#7D7D7D",
	"saisei": "#7D7D7D",
	"mirai": "#7D7D7D",
	"kaikaku": "#7D7D7D",
	"seishin": "#7D7D7D",
	"mushozoku": "#7D7D7D",
}

# 年齢区分のラベル
age_labels = {
	18: "18-19歳",
	20: "20代",
	30: "30代", 
	40: "40代",
	50: "50代",
	60: "60代",
	70: "70代以上"
}

# 政党得票率データ
# n: 政党キー: n才からn+9才までの政党得票率（18は18,19才, 70は70才以上）
vote_rate={
	18: {
		"jimin": 13.4,
		"komei": 3.6,
		"rikken": 8.1,
		"ishin": 4.9,
		"kokumin":23.4,
		"reiwa": 6.3,
		"kyosan": 3.3,
		"sansei": 23.2,
		"hoshu": 5.2,
		"shamin": 0.9,
		"nhk": 1.1,
		"saisei": 1,
		"mirai": 3.4,
		"kaikaku": 0.2,
		"seishin": 0.4,
		"mushozoku": 0.8,
	},
	20: {
		"jimin": 11.3,
		"komei": 3.4,
		"rikken": 7.2,
		"ishin": 4.8,
		"kokumin": 24.7,
		"reiwa": 6.4,
		"kyosan": 3.1,
		"sansei": 24.2,
		"hoshu": 6.6,
		"shamin": 0.9,
		"nhk": 0.9,
		"saisei": 0.8,
		"mirai": 3.8,
		"kaikaku": 0.1,
		"seishin": 0.3,
		"mushozoku": 0.6,
	},
	30: {
		"jimin": 12.6,
		"komei": 3.9,
		"rikken": 7.4,
		"ishin": 5.8,
		"kokumin": 18.7,
		"reiwa": 8.6,
		"kyosan": 2.5,
		"sansei": 23.2,
		"hoshu": 6.8,
		"shamin": 1,
		"nhk": 1.3,
		"saisei": 1.1,
		"mirai": 5,
		"kaikaku": 0.1,
		"seishin": 0.5,
		"mushozoku": 0.9,
	},
	40: {
		"jimin": 16.1,
		"komei": 4.6,
		"rikken": 9.2,
		"ishin": 7.4,
		"kokumin": 14.2,
		"reiwa": 11.6,
		"kyosan": 3,
		"sansei": 18.7,
		"hoshu": 5.8,
		"shamin": 1.1,
		"nhk": 1.4,
		"saisei": 1.2,
		"mirai": 3,
		"kaikaku": 0.1,
		"seishin": 0.8,
		"mushozoku": 1.1,
	},
	50: {
		"jimin": 20.6,
		"komei": 5.5,
		"rikken": 11.8,
		"ishin": 7.5,
		"kokumin": 11.7,
		"reiwa": 10.7,
		"kyosan": 3.2,
		"sansei": 15.3,
		"hoshu": 5.2,
		"shamin": 1.6,
		"nhk": 1.4,
		"saisei": 1,
		"mirai": 1.8,
		"kaikaku": 0.1,
		"seishin": 1,
		"mushozoku": 0.7,
	},
	60: {
		"jimin": 26.3,
		"komei": 7.8,
		"rikken": 15.8,
		"ishin": 6.8,
		"kokumin": 8.8,
		"reiwa": 6.5,
		"kyosan": 4.4,
		"sansei": 11.6,
		"hoshu": 4.2,
		"shamin": 2.6,
		"nhk": 1.1,
		"saisei": 0.9,
		"mirai": 1.1,
		"kaikaku": 0.1,
		"seishin": 0.8,
		"mushozoku": 0.6,
	},
	70: {
		"jimin": 36.9,
		"komei": 8.7,
		"rikken": 19.9,
		"ishin": 5.8,
		"kokumin": 5.7,
		"reiwa": 2.7,
		"kyosan": 7,
		"sansei": 5.5,
		"hoshu": 1.9,
		"shamin": 2.9,
		"nhk": 0.5,
		"saisei": 0.5,
		"mirai": 0.4,
		"kaikaku": 0.1,
		"seishin": 0.5,
		"mushozoku": 0.4,
	},
}

import matplotlib.pyplot as plt
import matplotlib as mpl
import platform
import numpy as np

# 日本語フォント設定（Windows環境に特化）
if platform.system() == 'Windows':
    plt.rcParams['font.family'] = ['Yu Gothic', 'Meiryo', 'MS Gothic']
else:
    plt.rcParams['font.family'] = ['DejaVu Sans']

plt.rcParams['axes.unicode_minus'] = False  # マイナス記号の文字化けを防ぐ

# フォントサイズの調整
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8

from common_calculations import calculate_age_populations as calc_age_populations, calculate_party_votes_for_ages, population

def calculate_age_populations():
	"""年齢区分ごとの人口を計算する共通関数"""
	return calc_age_populations()

def plot_population(subplot_pos=1):
	# 年齢区分ごとの人口を計算
	age_populations = calculate_age_populations()
	
	# 総人口を計算
	total_population = sum(age_populations.values())
	
	# 人口比を計算
	population_ratios = {age: pop / total_population * 100 for age, pop in age_populations.items()}
	
	# サブプロットを作成（指定された位置に）
	plt.subplot(3, 3, subplot_pos)  # 3行3列のグリッドで配置
	
	# データを準備
	ages = list(population_ratios.keys())
	ratios = list(population_ratios.values())
	labels = [age_labels[age] for age in ages]
	
	# 各年齢区分に異なる色を設定
	colors = plt.cm.Set3(np.linspace(0, 1, len(ages)))
	
	# 横に積み上げる帯グラフを作成
	bottom = 0
	bars = []
	for i, (age, ratio) in enumerate(zip(ages, ratios)):
		bar = plt.barh(0, ratio, left=bottom, color=colors[i], alpha=0.8, height=0.6, label=f'{age_labels[age]}: {ratio:.1f}%')
		bars.append(bar)
		bottom += ratio
	
	# グラフの設定
	plt.title('年齢区分別人口比率', fontsize=10, fontweight='bold')
	plt.xlim(0, 100)
	
	# 軸の目盛りを削除
	plt.xticks([])
	plt.yticks([])
	
	# グリッドを追加
	plt.grid(axis='x', alpha=0.3)
	
	# 凡例を表示（サイズを大きく）
	plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
	
	print("年齢区分別人口比率:")
	for age, ratio in population_ratios.items():
		print(f"{age_labels[age]}: {ratio:.1f}%")

def plot_party_vote_rate_for_selected_ages(selected_ages=None, subplot_pos=1):
	# 年齢区分ごとの人口を計算
	age_populations = calculate_age_populations()
	
	# 選択された年齢区分を決定
	if selected_ages is None:
		# デフォルトではすべての年齢区分を使用
		selected_ages = list(vote_rate.keys())
	
	# 共通関数を使用して政党別得票率を計算
	all_party_votes, selected_population, population_ratios = calculate_party_votes_for_ages(
		selected_ages, age_populations, vote_rate, parties
	)
	
	# 全国民の場合は独立した図を作成
	if selected_ages == list(vote_rate.keys()):
		plt.figure(figsize=(12, 8))
		plt.subplot(1, 1, 1)
	else:
		# サブプロットを作成（指定された位置に）
		plt.subplot(3, 3, subplot_pos)
	
	# データを準備
	parties_list = list(all_party_votes.keys())
	rates = list(all_party_votes.values())
	labels = [parties[party] for party in parties_list]
	
	# 各政党に手動で指定した色を設定
	colors = [party_colors[party] for party in parties_list]
	
	# 横に積み上げる帯グラフを作成
	bottom = 0
	bars = []
	for i, (party, rate) in enumerate(zip(parties_list, rates)):
		bar = plt.barh(0, rate, left=bottom, color=colors[i], alpha=0.8, height=0.6, label=f'{parties[party]}: {rate:.1f}%')
		bars.append(bar)
		bottom += rate
	
	# タイトルを動的に生成
	if selected_ages == list(vote_rate.keys()):
		title = '全国民の政党別得票率'
		print_title = "全国民の政党別得票率:"
	elif len(selected_ages) == 1:
		age_key = selected_ages[0]
		title = f'{age_labels[age_key]}の政党別得票率'
		print_title = f"{age_labels[age_key]}の政党別得票率:"
	else:
		selected_age_labels = [age_labels[age] for age in selected_ages if age in age_labels]
		title = f'選択年齢区分の政党別得票率 ({", ".join(selected_age_labels)})'
		print_title = f"選択年齢区分の政党別得票率 ({', '.join(selected_age_labels)}):"
	
	# グラフの設定
	plt.title(title, fontsize=10, fontweight='bold')
	plt.xlim(0, 100)
	
	# 軸の目盛りを削除
	plt.xticks([])
	plt.yticks([])
	
	# グリッドを追加
	plt.grid(axis='x', alpha=0.3)
	
	# 凡例を表示（全国民の場合のみ）
	if selected_ages == list(vote_rate.keys()):
		plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8)
	
	print(print_title)
	for party, rate in all_party_votes.items():
		print(f"  {parties[party]}: {rate:.1f}%")

def main():
	# 人口比率グラフを独立した図として作成
	plt.figure(figsize=(12, 8))
	plot_population(subplot_pos=1)
	plt.tight_layout()
	
	# 政党別得票率グラフを別の図として作成
	plt.figure(figsize=(24, 18))  # サイズを大きくして余白を確保
	
	# を配置
	# 3行3列のグリッドで配置：位置1は人口比率、位置2-8は各年齢区分
	for i, age in enumerate(vote_rate.keys()):
		# 位置2から順番に配置（位置1は人口比率グラフ）
		subplot_pos = i + 1  # 位置1から開始
		plot_party_vote_rate_for_selected_ages(selected_ages=[age], subplot_pos=subplot_pos)

	# 全国民の政党別得票率は別の図として表示
	plot_party_vote_rate_for_selected_ages()

	# 余白を調整してから表示
	plt.subplots_adjust(left=0.15, right=0.83, top=0.92, bottom=0.1, hspace=0.5, wspace=0.5)
	
	# すべてのグラフを同時に表示
	plt.show()

if __name__ == "__main__":
	main()