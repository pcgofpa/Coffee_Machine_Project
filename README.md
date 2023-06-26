<h1>Coffee Machine Project</h1>

<h2> Description </h2>
 
Project for a user placing a coffee order. Program will prompt user for order, and calculate 
a total. User will input a payment amount and the program will calculate the change.

<h2> Requirements </h2>
<ol>
    <li>Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        <ol>
            <li>Check the user’s input to decide what to do next.</li>
            <li>The prompt should show every time action has completed, e.g. once the drink is
                dispensed. The prompt should show again to serve the next customer.</li>
        </ol>
    </li>
    <li>Turn off the Coffee Machine by entering “off” to the prompt.
        <ol>
            <li>For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. 
                Your code should end execution when this happens.
            </li>
        </ol>
    </li>
    <li>Print report.
        <ol>
            <li>When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
                <br>Water: 100ml
                <br>Milk: 50ml
                <br>Coffee: 76g
                <br>Money: $2.5
            </li>
        </ol>
    </li>
    <li>Check resources sufficient?
        <ol>
            <li>When the user chooses a drink, the program should check if there are enough resources to make that drink.</li>
            <li>E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: 
                “Sorry there is not enough water.” </li>
            <li>The same should happen if another resource is depleted, e.g. milk or coffee.</li>
        </ol>
    </li>
    <li>Process coins.
        <ol>
            <li>If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.</li>
            <li>Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01</li>
            <li>Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52</li>
        </ol>
    </li>
    <li>Check transaction successful?
        <ol>
            <li>Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they only inserted $0.52 then after counting 
                the coins the program should say “Sorry that's not enough money. Money refunded.”. </li>
            <li>But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time 
                “report” is triggered. E.g.
                <br>Water: 100ml
                <br>Milk: 50ml
                <br>Coffee: 76g
                <br>Money: $2.5</li>
            <li>If the user has inserted too much money, the machine should offer change.
                <br>E.G. "Here is $2.45 dollars in change." The change should be rounded to 2 decimal places.</li>
        </ol>
    </li>
    <li>Make Coffee
    <ol>
        <li>If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be 
            deducted from the coffee machine resources.<br><br>
            E.g. report before purchasing latte:<br>
            Water: 300ml<br>
            Milk: 200ml<br>
            Coffee: 100g<br>
            Money: $0<br><br>
            Report after purchasing latte:<br>
            Water: 100ml<br>
            Milk: 50ml<br>
            Coffee: 76g<br>
            Money: $2.5<br>
        </li>
        <li>Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.</li>
    </ol>
    </li>
</ol>
 
