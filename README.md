<h1>Expense Tracker Application</h1>
<p>A simple command-line application to manage your finances. This application allows users to add, delete, and view their expenses, as well as providing a summary of expenses.</p>

<h2>Features</h2>
<ul>
    <li>Add an expense with a description and amount.</li>
    <li>Delete an expense.</li>
    <li>View all expenses.</li>
    <li>View a summary of all expenses.</li>
    <li>View a summary of expenses for a specific month (of the current year).</li>
    <li>Expense categories and filter expenses by category.</li>
  
</ul>

<h2>Command List</h2>

<pre><code>
$ python main.py add --description "Lunch" --amount "20" --type "Food" 
# Expense added for Food
</code></pre>

<pre><code>
$ python main.py add --description "Car Washes" --amount 10 --type "Car"
# Expense added for Car
</code></pre>

<pre><code>
$ python main.py list

CAR
  
+------+----------+---------------+----------+
|   id | date     | description   |   amount |
+======+==========+===============+==========+
|    3 | 10/23/24 | Car washes    |       35 |
+------+----------+---------------+----------+
|    4 | 10/23/24 | Car washes    |       45 |
+------+----------+---------------+----------+
</code></pre>

<pre><code>
$ python main.py summary --type Car
80  dollars spent on  Car
</code></pre>
<pre><code>
$ python main.py delete --id 1
2 is deleted
</code></pre>
<pre><code>
$ python main.py summary --month 10
80 dollars spen in the 8th month
</code></pre>


<h2>Getting Started</h2>
<p>Clone the repository and navigate to the project directory:</p>
<pre><code>
git clone https://github.com/Haknozer/ExpenseTracker.git
cd ExpenseTracker
</code></pre>

<p>Run the application:</p>
<pre><code>python main.py</code></pre>

<h2>Contributing</h2>
<p>Feel free to submit issues or pull requests. Your contributions are welcome!</p>
https://roadmap.sh/projects/expense-tracker
