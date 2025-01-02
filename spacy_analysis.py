import spacy
nlp = spacy.load("en_core_web_sm")

def analyze_text(text):
    # テキストを解析
    doc = nlp(text)

    # トークンごとの詳細情報
    print("=== トークン解析 ===")
    for token in doc:
        print(f"Text: {token.text}, POS: {token.pos_}, Dependency: {token.dep_}, Lemma: {token.lemma_}")

    # 名詞句の抽出
    print("\n=== 名詞句 ===")
    for chunk in doc.noun_chunks:
        print(chunk.text)

    # 動詞の抽出
    print("\n=== 動詞 ===")
    for token in doc:
        if token.pos_ == "VERB":
            print(token.text)

    # 日付やエンティティの抽出
    print("\n=== 固有表現 ===")
    for ent in doc.ents:
        print(f"Text: {ent.text}, Label: {ent.label_}")

    # 依存関係をブラウザで表示
    try:
        from spacy import displacy
        displacy.serve(doc, style="dep", auto_select_port=True)
    except ImportError:
        print("\nDisplacy visualization is not available. Install the necessary library if needed.")

if __name__ == "__main__":
    # 英文
    text = "I write programming."
    analyze_text(text)
