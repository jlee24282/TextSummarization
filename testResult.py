import pandas as pd
from PyRouge.pyrouge import Rouge

data = pd.read_csv('data/output/output.csv')
r = Rouge()

# for row in data.iterrows():
#     system_generated_summary = row[1]['result']
#     manual_summmary = row[1]['summarizedL']
#     [precision, recall, f_score] = r.rouge_l([system_generated_summary], [manual_summmary])
#     print("Precision is :" + str(precision) + " Recall is :" + str(recall) + " F Score is :" + str(f_score))


from pythonrouge.pythonrouge import Pythonrouge
# system summary & reference summary
average1 = 0
average2 = 0
average3 = 0
total = len(data)
highest = 0
lowest = 10000
index = 0
for row in data.iterrows():
    summary = [[row[1]['result']]]
    reference = [[[row[1]['summarizedL']]]]
    rouge = Pythonrouge(summary_file_exist=False,
                        summary=summary, reference=reference,
                        n_gram=3, ROUGE_SU4=False, ROUGE_L=False,
                        recall_only=True, stemming=True, stopwords=True,
                        word_level=False, length_limit=False, length=50,
                        use_cf=True, cf=95, scoring_formula='average',
                        resampling=True, samples=1000, favor=False, p=0.8)
    score = rouge.calc_score()
    print score, row[1]['topic']
    index += 1
    average1 += score['ROUGE-1']
    average2 += score['ROUGE-2']
    average3 += score['ROUGE-3']
    if highest < score['ROUGE-1']:
        highest = score['ROUGE-1']
    if lowest > score['ROUGE-1']:
        lowest = score['ROUGE-1']

average1 = average1/total
average2 = average2/total
average3 = average3/total

# print 'Overal Average (ROUGE-1-F): ', averageF
print 'Overall Average (ROUGE-1): ', average1
print 'Overall Average (ROUGE-2): ', average2
print 'Overall Average (ROUGE-3): ', average3
print 'Highest (ROUGE-1-R): ', highest
print 'Lowest (ROUGE-1-R): ', lowest
