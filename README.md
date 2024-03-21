## Flask Application Design for an Optimization Teaching Website

### HTML Files

- **home.html**: Homepage of the website, providing an overview of optimization and its applications.
- **concepts.html**: Explains fundamental optimization concepts such as linear programming, dynamic programming, and gradient descent.
- **algorithms.html**: Explores various optimization algorithms, including simplex method, interior point method, and evolutionary algorithms.
- **applications.html**: Demonstrates real-world applications of optimization in fields like finance, engineering, and logistics.
- **exercises.html**: Provides interactive exercises and challenges to reinforce understanding.

### Routes

- **@app.route('/')**: Home page route, rendering the `home.html` file.
- **@app.route('/concepts')**: Concepts route, rendering the `concepts.html` file.
- **@app.route('/algorithms')**: Algorithms route, rendering the `algorithms.html` file.
- **@app.route('/applications')**: Applications route, rendering the `applications.html` file.
- **@app.route('/exercises')**: Exercises route, rendering the `exercises.html` file.
- **@app.route('/submit_exercise')**: Route to handle exercise submissions and provide feedback (if applicable).