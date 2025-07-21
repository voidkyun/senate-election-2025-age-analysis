#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
共通計算処理モジュール
年齢区分別の得票率計算で使用される共通関数とデータを提供
"""

# 人口データ
# n: n才からn+4才までの人口（85は85才以上）
population={
	0: 4541,
	5: 5114,
	10: 5376,
	15: 5706,
	20: 6320,
	25: 6384,
	30: 6714,
	35: 7498,
	40: 8476,
	45: 9868,
	50: 8738,
	55: 7940,
	60: 7442,
	65: 8236,
	70: 9189,
	75: 7065,
	80: 5404,
	85: 6133,
}

def calculate_age_populations(population_data=None):
    """年齢区分ごとの人口を計算する共通関数"""
    if population_data is None:
        population_data = population
    
    age_populations = {}
    
    # 18,19歳の人口（15歳から19歳の人口を2/5倍）
    age_populations[18] = population_data[15] * (2/5)
    
    # 各年代の人口を計算
    for age in [20, 30, 40, 50, 60]:
        # 各年代は10歳の範囲なので、対応する5歳区分を2つずつ合計
        age_populations[age] = population_data[age] + population_data[age + 5]
    
    # 70代以上の人口（70-74歳 + 75-79歳 + 80-84歳 + 85歳以上）
    age_populations[70] = population_data[70] + population_data[75] + population_data[80] + population_data[85]
    
    return age_populations

def calculate_party_votes_for_ages(selected_ages, age_populations, vote_rate, parties):
    """
    選択された年齢区分の政党別得票率を計算する共通関数
    
    Parameters:
    - selected_ages: 選択された年齢区分のリスト
    - age_populations: 年齢区分ごとの人口辞書
    - vote_rate: 年齢区分ごとの政党別得票率辞書
    - parties: 政党辞書
    
    Returns:
    - all_party_votes: 計算された政党別得票率辞書
    - selected_population: 選択された年齢区分の総人口
    - population_ratios: 選択された年齢区分の人口比辞書
    """
    # 選択された年齢区分の人口のみを合計
    selected_population = sum(age_populations[age] for age in selected_ages if age in age_populations)
    
    # 選択された年齢区分の人口比を計算
    population_ratios = {age: age_populations[age] / selected_population for age in selected_ages if age in age_populations}
    
    # 選択された年齢区分の政党別得票率を計算
    all_party_votes = {}
    
    # 各政党の得票率を初期化
    for party in parties.keys():
        all_party_votes[party] = 0
    
    # 選択された年齢区分の得票率を人口比で重み付けして合計
    for age_key in selected_ages:
        if age_key in vote_rate and age_key in population_ratios:
            age_vote_data = vote_rate[age_key]
            age_pop_ratio = population_ratios[age_key]
            
            for party, vote_rate_value in age_vote_data.items():
                all_party_votes[party] += vote_rate_value * age_pop_ratio
    
    return all_party_votes, selected_population, population_ratios

def get_age_groups(vote_rate):
    """年齢区分のリストを取得する共通関数"""
    return sorted(vote_rate.keys()) 