
import streamlit as st
st.title('運用プラン診断')
st.header('あなたにぴったりな運用プランを確認しましょう')
st.text('６つの質問に答えてるだけで最適な資産配分を確認することができます')

q1 = st.radio(
    "質問１〜年齢を教えてください", 
    ('20代',
     '30代',
     '40代',
     '50代',
     '60代以上'))

'あなたの年齢は',q1,'です'

if q1 == '20代': 
  q1_score = 5
elif q1 == '30代': 
  q1_score = 4
elif q1 == '40代': 
  q1_score = 3
elif q1 == '50代': 
  q1_score = 2
else: 
  q1_score = 1

'スコアは',q1_score,'です'

q2 = st.radio(
    "質問２〜金融知識の理解レベルを教えてください", 
    ('初級',
     '初中級',
     '中級',
     '中上級',
     '上級'))

'あなたの理解レベルは',q2,'です'

if q2 == '初級': 
  q2_score = 1
elif q2 == '初中級': 
  q2_score = 2
elif q2 == '中級': 
  q2_score = 3
elif q2 == '中上級': 
  q2_score = 4
else: 
  q2_score = 5

'スコアは',q2_score,'です'


q3 = st.radio(
    "質問3〜何年間投資するご予定ですか", 
    ('5年未満',
     '5〜10年',
     '10〜15年',
     '15〜20年',
     '20年以上'))

'あなたの投資期間は',q3,'です'

if q3 == '5年未満': 
  q3_score = 1
elif q3 == '5〜10年': 
  q3_score = 2
elif q3 == '10〜15年': 
  q3_score = 3
elif q3 == '15〜20年': 
  q3_score = 4
else: 
  q3_score = 5

'スコアは',q3_score,'です'


q4 = st.radio(
    "質問4〜投資の目的について教えてください", 
    ('投資元本の安定性重視',
     '元本の安全性と安定収入',
     '利子配当などの定期的な収入を重視',
     '定期的な収入を重視するが、投資しさんの値上がり益も追求',
     '投資資産価値の大幅増大を優先'))

'あなたの投資目的は',q4,'です'

if q4 == '投資元本の安定性重視': 
  q4_score = 1
elif q4 == '元本の安全性と安定収入': 
  q4_score = 2
elif q4 == '利子配当などの定期的な収入を重視': 
  q4_score = 3
elif q4 == '定期的な収入を重視するが、投資しさんの値上がり益も追求': 
  q4_score = 4
else: 
  q4_score = 5

'スコアは',q4_score,'です'


q5 = st.radio(
    "質問5〜年収を教えてください", 
    ('300万円未満',
     '300万円〜500万円',
     '500万円〜1000万円',
     '1000万円〜1500万円',
     '1500万円以上'))

'あなたの年収は',q5,'です'

if q5 == '300万円未満': 
  q5_score = 1
elif q5 == '300万円〜500万円': 
  q5_score = 2
elif q5 == '500万円〜1000万円': 
  q5_score = 3
elif q5 == '1000万円〜1500万円': 
  q5_score = 4
else: 
  q5_score = 5

'スコアは',q5_score,'です'


q6 = st.radio(
    "質問6〜金融資産を教えてください", 
    ('500万円未満',
     '500万円〜1000万円',
     '1000万円〜5000万円',
     '5000万円〜10000万円',
     '10000万円以上'))

'あなたの金融資産は',q6,'です'

if q6 == '500万円未満': 
  q6_score = 1
elif q6 == '500万円〜1000万円': 
  q6_score = 2
elif q6 == '1000万円〜5000万円': 
  q6_score = 3
elif q6 == '5000万円〜10000万円': 
  q6_score = 4
else: 
  q6_score = 5

'スコアは',q6_score,'です'


q7 = st.radio(
    "質問7〜金融資産のうち投資可能な割合", 
    ('10%',
     '30%',
     '50%',
     '80%',
     '100%'))

'あなたの金融資産のうち投資可能な割合は',q7,'です'

if q7 == '10%': 
  q7_score = 1
elif q7 == '30%': 
  q7_score = 2
elif q7 == '50%': 
  q7_score = 3
elif q7 == '80%': 
  q7_score = 4
else: 
  q7_score = 5

'スコアは',q7_score,'です'


q8 = st.radio(
    "質問8〜相場の急激な下落に対して、どのくらいの下落であれば許容できますか？", 
    ('5%未満',
     '5〜10%',
     '10〜25%',
     '25〜50%',
     '50%以上'))

'あなたの金融資産のうち投資可能な割合は',q8,'です'

if q8 == '5%未満': 
  q8_score = 1
elif q8 == '5〜10%': 
  q8_score = 2
elif q8 == '10〜25%': 
  q8_score = 3
elif q8 == '25〜50%': 
  q8_score = 4
else: 
  q8_score = 5

'スコアは',q8_score,'です'

t_score = q1_score + q2_score + q3_score + q4_score + q5_score + q6_score + q7_score + q8_score

'トータルスコアは',t_score,'です'
