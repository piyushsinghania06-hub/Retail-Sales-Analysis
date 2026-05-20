from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

def sales_prediction(df):

    X = df[['Quantity', 'Profit']]
    y = df['Sales']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    error = mean_absolute_error(y_test, predictions)

    print("Mean Absolute Error:", error)

    # Plot
    plt.figure(figsize=(8,5))
    plt.scatter(y_test, predictions)
    plt.xlabel("Actual Sales")
    plt.ylabel("Predicted Sales")
    plt.title("Sales Prediction")
    plt.savefig('images/prediction_graph.png')
    plt.show()
