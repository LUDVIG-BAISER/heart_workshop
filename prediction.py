import argparse
import pandas as pd
import joblib


def load_model(model_path):
    return joblib.load(model_path)


def predict_and_save(input_csv, model_path, output_csv):
    df_test = pd.read_csv(input_csv)
    model = load_model(model_path)
    predictions = model.predict(df_test)
    result = pd.DataFrame({
        'id': df_test['id'],
        'prediction': predictions
    })
    result.to_csv(output_csv, index=False)
    print(f"Предсказания: {output_csv}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=True)
    parser.add_argument('--model', type=str, default='model_best_recall.pkl')
    parser.add_argument('--output', type=str, default='submission.csv')

    args = parser.parse_args()
    predict_and_save(args.input, args.model, args.output)


if __name__ == '__main__':
    main()
