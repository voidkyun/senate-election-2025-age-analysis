import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import platform

# 日本語フォント設定（Windows環境に特化）
if platform.system() == 'Windows':
    plt.rcParams['font.family'] = ['Yu Gothic', 'Meiryo', 'MS Gothic']
else:
    plt.rcParams['font.family'] = ['DejaVu Sans']

plt.rcParams['axes.unicode_minus'] = False

# データのインポート
from graph import parties, vote_rate, age_labels, party_colors
from common_calculations import calculate_age_populations, calculate_party_votes_for_ages, get_age_groups, population

def create_detailed_age_animation(interval=2000, repeat=True, save_gif=False, filename="age_animation.gif"):
    """
    年齢制限を段階的に変更しながら得票数の変化をアニメーションで表現
    
    Parameters:
    - interval: フレーム間の間隔（ミリ秒）
    - repeat: アニメーションを繰り返すかどうか
    - save_gif: GIFファイルとして保存するかどうか
    - filename: 保存するファイル名
    """
    
    # アニメーション設定
    FPS = 30  # フレームレート
    INTERPOLATION_DURATION = 0.5  # 補間時間（秒）
    PAUSE_DURATION = 1.0  # 停止時間（秒）
    
    # フレーム数を計算
    interpolation_frames = int(FPS * INTERPOLATION_DURATION)  # 補間フレーム数
    pause_frames = int(FPS * PAUSE_DURATION)  # 停止フレーム数
    
    # 年齢区分ごとの人口を計算
    age_populations = calculate_age_populations()
    
    # 年齢区分のリスト（昇順）
    age_groups = get_age_groups(vote_rate)
    
    # 各フレーム（年齢制限）での得票率を計算
    frames_data = []
    

    
    for i, max_age in enumerate(age_groups):
        # 現在の年齢制限までの年齢区分を選択
        selected_ages = age_groups[:i+1]
        
        # 共通関数を使用して政党別得票率を計算
        all_party_votes, selected_population, population_ratios = calculate_party_votes_for_ages(
            selected_ages, age_populations, vote_rate, parties
        )
        
        # 補間フレームを追加
        for frame in range(interpolation_frames):
            # 補間係数を計算（0から1の間）
            alpha = frame / interpolation_frames
            
            # 前のフレームのデータを取得（最初のフレーム以外）
            if i > 0 and frame == 0:
                prev_selected_ages = age_groups[:i]
                prev_party_votes, prev_population, _ = calculate_party_votes_for_ages(
                    prev_selected_ages, age_populations, vote_rate, parties
                )
            elif i > 0:
                prev_selected_ages = age_groups[:i]
                prev_party_votes, prev_population, _ = calculate_party_votes_for_ages(
                    prev_selected_ages, age_populations, vote_rate, parties
                )
            else:
                prev_party_votes = {party: 0 for party in parties.keys()}
                prev_population = 1  # ゼロ除算を防ぐために1に設定
            
            # 補間されたデータを計算
            interpolated_party_votes = {}
            for party in parties.keys():
                current_rate = all_party_votes.get(party, 0)
                prev_rate = prev_party_votes.get(party, 0)
                interpolated_party_votes[party] = prev_rate + (current_rate - prev_rate) * alpha
            
            interpolated_population = prev_population + (selected_population - prev_population) * alpha
            
            frames_data.append({
                'selected_ages': selected_ages,
                'party_votes': interpolated_party_votes,
                'max_age': max_age,
                'total_population': interpolated_population,
                'alpha': alpha
            })
        
        # 補完完了後の停止フレームを追加
        for pause_frame in range(pause_frames):
            frames_data.append({
                'selected_ages': selected_ages,
                'party_votes': all_party_votes,
                'max_age': max_age,
                'total_population': selected_population,
                'alpha': 1.0,
                'is_pause': True
            })
    
    # アニメーション用の図を作成
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(24, 12), gridspec_kw={'height_ratios': [3, 1]})
    
    # 政党名のリスト
    parties_list = list(parties.keys())
    party_labels = [parties[party] for party in parties_list]
    
    # 各政党に手動で指定した色を設定
    colors = [party_colors[party] for party in parties_list]
    
    # バーの位置（帯グラフ用）
    y_pos = 0  # 1つのバーに積み上げる
    
    # 初期バーを作成（帯グラフ用）
    bars = []
    for i in range(len(parties_list)):
        bar = ax1.barh(y_pos, 0, left=0, color=colors[i], alpha=0.8, height=0.8)
        bars.append(bar[0])
    
    # メイングラフの設定
    ax1.set_yticks([y_pos])
    ax1.set_yticklabels([])  # ラベルを削除
    ax1.grid(axis='x', alpha=0.3)
    ax1.set_xlim(0, 100)  # 積み上げなので100%まで表示
    
    # 軸の目盛りとラベルを削除
    ax1.set_xticks([])
    ax1.set_xlabel('')
    ax1.set_ylabel('')
    
    # 凡例用のハンドルとラベルを初期化
    legend_handles = []
    legend_labels = []
    for i, party in enumerate(parties_list):
        legend_handles.append(plt.Rectangle((0, 0), 1, 1, facecolor=colors[i], alpha=0.8))
        legend_labels.append(f'{parties[party]}: 0.0%')
    
    # 凡例を追加
    legend = ax1.legend(legend_handles, legend_labels, bbox_to_anchor=(1.02, 1), 
                        loc='upper left', fontsize=8, ncol=1)
    
    # タイトル用のテキスト
    title_text = fig.suptitle('', fontsize=16, fontweight='bold', y=0.95)
    
    # 人口比率グラフ（下部）- 帯グラフ用
    population_bars = []
    population_colors = plt.cm.Set3(np.linspace(0, 1, len(age_groups)))
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.grid(axis='x', alpha=0.3)
    ax2.set_xlim(0, 100)
    ax2.set_ylim(0, 1)
    
    # 軸のラベルを削除
    ax2.set_xlabel('')
    ax2.set_ylabel('')
    
    # 人口比率のタイトル
    population_title = ax2.text(0.5, 0.95, '対象年齢区分の人口比率', transform=ax2.transAxes, 
                                ha='center', va='top', fontsize=10, fontweight='bold')
    
    def animate(frame):
        """アニメーションの各フレームを更新"""
        frame_data = frames_data[frame]
        party_votes = frame_data['party_votes']
        selected_ages = frame_data['selected_ages']
        max_age = frame_data['max_age']
        total_population = frame_data['total_population']
        
        # メイングラフのバーの幅を更新（帯グラフ）
        rates = [party_votes[party] for party in parties_list]
        left = 0
        for i, (bar, rate) in enumerate(zip(bars, rates)):
            bar.set_width(rate)
            bar.set_x(left)
            left += rate
        
        # タイトルを更新
        alpha = frame_data.get('alpha', 1.0)  # 補間係数を取得
        
        title = f'{age_labels[max_age]}以下の得票率'
        
        title_text.set_text(title)
        
        # 既存のテキストを完全に削除（メイングラフ）
        for artist in ax1.texts[:]:  # コピーを作成してイテレート
            artist.remove()
        
        # 値のラベルは表示しない（graph.pyと同様）
        pass
        
        # 凡例を更新
        for i, (party, rate) in enumerate(zip(parties_list, rates)):
            legend_labels[i] = f'{parties[party]}: {rate:.1f}%'
            legend.get_texts()[i].set_text(legend_labels[i])
        
        # 既存の人口比率テキストを完全に削除（年代名を追加する前に実行）
        for artist in ax2.texts[:]:  # コピーを作成してイテレート
            if artist != population_title:
                artist.remove()
        
        # 人口比率グラフを更新（帯グラフ）
        # 既存のバーを削除
        for bar in population_bars:
            bar.remove()
        population_bars.clear()
        
        # 選択された年齢区分の人口比率を計算
        selected_population_ratios = []
        for age in age_groups:
            if age in selected_ages and total_population > 0:
                ratio = (age_populations[age] / total_population) * 100
                selected_population_ratios.append(ratio)
            else:
                selected_population_ratios.append(0)
        
        # 帯グラフを作成
        bottom = 0
        for i, (age, ratio) in enumerate(zip(age_groups, selected_population_ratios)):
            if ratio > 0:
                bar = ax2.barh(0, ratio, left=bottom, color=population_colors[i], 
                               alpha=0.8, height=0.6)
                population_bars.append(bar)
                
                # 年代名をバー内に表示
                ax2.text(bottom + ratio/2, 0.5, age_labels[age], 
                            ha='center', va='center', fontsize=8, fontweight='bold')
                
                bottom += ratio
        
        # 人口比率の値ラベルは表示しない（graph.pyと同様）
        pass
        
        return bars, population_bars
    
    # アニメーションを作成（FPSに基づいて間隔を計算）
    frame_interval = int(1000 / FPS)  # ミリ秒単位の間隔
    anim = animation.FuncAnimation(fig, animate, frames=len(frames_data), 
                                  interval=frame_interval, repeat=repeat, blit=False)
    
    # GIFとして保存する場合
    if save_gif:
        print(f"アニメーションを {filename} として保存中...")
        anim.save(filename, writer='pillow', fps=FPS)
        print(f"保存完了: {filename}")
    
    plt.subplots_adjust(right=0.85, left=0.1, top=0.95, bottom=0.1)  # 凡例のためのスペースを確保
    plt.show()
    
    return anim



def create_animation_with_save(filename="age_animation.gif", interval=2000):
    """アニメーションをGIFファイルとして保存"""
    # ファイル名に拡張子がない場合は.gifを追加
    if not filename.endswith('.gif'):
        filename = filename + '.gif'
    
    print(f"アニメーションを {filename} として保存します...")
    return create_detailed_age_animation(interval=interval, repeat=True, save_gif=True, filename=filename)

if __name__ == "__main__":
    print("年齢制限アニメーションを開始します...")
    print("1. 詳細なアニメーション（人口比率付き）")
    print("2. GIFファイルとして保存")
    
    choice = input("選択してください (1-2): ").strip()
    
    if choice == "1":
        create_detailed_age_animation()
    elif choice == "2":
        filename = input("保存するファイル名を入力してください (デフォルト: age_animation.gif): ").strip()
        if not filename:
            filename = "age_animation.gif"
        create_animation_with_save(filename=filename)
    else:
        print("デフォルトで詳細なアニメーションを実行します...")
        create_detailed_age_animation() 