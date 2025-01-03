# 依存関係ラベル (Dependency Labels) の解説

このドキュメントでは、自然言語処理 (NLP) で使用される依存関係ラベルについて説明します。これらのラベルは文中の単語間の文法的な関係を示し、文構造の解析に役立ちます。

## 依存関係ラベルの説明

### 21. **nummod** (数詞修飾)
- **略さない言い方**: Numeric Modifier
- **意味**: 名詞を修飾する数詞や数量を示します。
- **例**: *I have two apples.* → `two` ("apples" を修飾)

### 22. **poss** (所有格修飾)
- **略さない言い方**: Possessive Modifier
- **意味**: 名詞を修飾する所有格を示します。
- **例**: *John's book is interesting.* → `John's` ("book" を修飾)

### 23. **expl** (形式主語)
- **略さない言い方**: Expletive
- **意味**: 形式主語（「そこに」「それは」など）を示します。
- **例**: *There is a book on the table.* → `There` (形式主語)

### 24. **parataxis** (並列構造)
- **略さない言い方**: Parataxis
- **意味**: 並列的な関係で結ばれた節や文を示します。
- **例**: *I came, I saw, I conquered.* → `I saw` (並列構造の一部)

### 25. **csubj** (節主語)
- **略さない言い方**: Clausal Subject
- **意味**: 動詞の主語が節である場合を示します。
- **例**: *What he said is true.* → `What he said` (節主語)

### 26. **csubjpass** (受動態節主語)
- **略さない言い方**: Clausal Passive Subject
- **意味**: 受動態で、主語が節である場合を示します。
- **例**: *That he lied was believed by everyone.* → `That he lied` (受動態節主語)

### 27. **auxpass** (受動態助動詞)
- **略さない言い方**: Auxiliary Passive
- **意味**: 受動態で使用される助動詞を示します。
- **例**: *The book was read by her.* → `was` (受動態助動詞)

### 28. **dep** (依存関係ラベル未定義)
- **略さない言い方**: Dependent
- **意味**: 特定の依存関係ラベルに分類されない語を示します。
- **例**: 特定の文脈による

### 20. **npadvmod** (名詞句の副詞修飾)
- **略さない言い方**: Noun Phrase Adverbial Modifier
- **意味**: 名詞句が副詞のように文全体や動詞を修飾する場合を示します。
- **例**: *Yesterday, I went to the park.* → `Yesterday` (文全体を修飾)

### 19. **appos** (同格)
- **意味**: 名詞を補足説明する名詞や句を示します。
- **例**: *My friend John is here.* → `John` ("friend" の同格として "John")

### 1. **nsubj** (主語)
- **意味**: 動詞の主語となる名詞や代名詞を示します。
- **例**: *I play soccer.* → `I` ("play" の主語)

### 2. **dobj** (直接目的語)
- **意味**: 動詞の対象となる名詞や代名詞を示します。
- **例**: *I play soccer.* → `soccer` ("play" の目的語)

### 3. **iobj** (間接目的語)
- **意味**: 動詞の間接的な対象を示します（通常「〜に」に相当）。
- **例**: *John gave Sarah a gift.* → `Sarah` ("gift" の受け取り手)

### 4. **ROOT** (文の中心)
- **意味**: 文の中心となる単語（通常は動詞）。
- **例**: *I play soccer.* → `play` (文の中心)

### 5. **amod** (形容詞修飾語)
- **意味**: 名詞を修飾する形容詞を示します。
- **例**: *The red ball.* → `red` ("ball" を修飾)

### 6. **advmod** (副詞修飾語)
- **意味**: 動詞や形容詞を修飾する副詞を示します。
- **例**: *He runs quickly.* → `quickly` ("runs" を修飾)

### 7. **prep** (前置詞)
- **意味**: 名詞や動詞に関連する前置詞を示します。
- **例**: *He is at the park.* → `at` (前置詞)

### 8. **pobj** (前置詞の目的語)
- **意味**: 前置詞の対象となる名詞を示します。
- **例**: *He is at the park.* → `park` ("at" の目的語)

### 9. **det** (限定詞)
- **意味**: 名詞の前にある「the」「a」などの限定詞を示します。
- **例**: *The ball.* → `The` ("ball" を修飾)

### 10. **compound** (複合名詞)
- **意味**: 他の名詞を修飾して複合名詞を形成する名詞を示します。
- **例**: *The soccer field.* → `soccer` ("field" を修飾)

### 11. **punct** (句読点)
- **意味**: 句読点（ピリオド、コンマなど）を示します。
- **例**: *I play soccer.* → `.` (句読点)

### 12. **nmod** (名詞修飾語)
- **意味**: 名詞を修飾する名詞句を示します。
- **例**: *The book on the table.* → `table` ("book" を修飾)

### 13. **attr** (属性)
- **意味**: 動詞`be`やそれに類似する動詞の補語（主語の状態や性質を説明する語）を示します。
- **例**: *She is smart.* → `smart` ("She" を説明)

### 14. **acl** (名詞修飾節)
- **意味**: 名詞を修飾する節（関係節など）。
- **例**: *The man who walks.* → `walks` ("man" を修飾)

### 15. **ccomp** (節補語)
- **意味**: 動詞を補完する節（主節と従属節が明確に関連する場合）。
- **例**: *I think he is coming.* → `coming` ("think" の補語)

### 16. **xcomp** (開いた節補語)
- **意味**: 主語が省略された動詞句を補完する節。
- **例**: *She wants to leave.* → `leave` ("wants" の補語)

### 17. **aux** (助動詞)
- **意味**: 動詞を補助する助動詞。
- **例**: *He is running.* → `is` ("running" を補助)

### 18. **neg** (否定修飾語)
- **意味**: 動詞や名詞を否定する語（例: not, no）。
- **例**: *He is not happy.* → `not` ("happy" を否定)

## 例文の解析

### 文: *John gave Sarah a gift.*
| **単語** | **品詞 (POS)** | **依存関係ラベル** | **説明**                 |
|----------|----------------|--------------------|-------------------------|
| John     | PROPN          | nsubj             | 主語 ("gave" の動作主) |
| gave     | VERB           | ROOT              | 文の中心               |
| Sarah    | PROPN          | iobj              | 間接目的語 (受け取り手) |
| a        | DET            | det               | 限定詞 ("gift" を修飾) |
| gift     | NOUN           | dobj              | 直接目的語 (与えられるもの) |

この解析により、文法構造と単語間の関係を理解することができます。

---

これらの依存関係ラベルを使用すると、文中の文法的な関係を分析し、自然言語処理のタスクに役立てることができます。

