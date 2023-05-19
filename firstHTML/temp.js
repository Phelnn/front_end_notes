// Task 1: Build a function-based console log message generator
function consoleStyler(color, background, fontSize, txt ) {
    var message = "%c" + txt
    var style = `color: ${color}`
    style += `background: ${background}`
    style += `font-size: ${fontSize}`
    console.log(message);
    console.log(style)
}

// Task 2: Build another console log message generator
function celebrateStyler(reason) {
    var fontStyle = "color: tomato; font-size:50px"
    
    if (reason == "birthday") {
        console.log(`%cHappy birthday`, fontStyle)
        console.log(fontStyle)
    }
    else if(reason == "champions") {
        console.log(`%cCongrats on the title!`, fontStyle)
    }
    else{
        console.log(`%cwhatever`, fontStyle)
    }
}


// Task 3: Run both the consoleStyler and the celebrateStyler functions
consoleStyler(`'#1d5c63'`, `'#ede6db'`, `'40px'`, `'Congrats!'`)
celebrateStyler('birthday')

// Task 4: Insert a congratulatory and custom message
function styleAndCelebrate(color, background, fontSize, txt, reason) {
    consoleStyler(color, background, fontSize, txt); 
    celebrateStyler(reason)
}


// Call styleAndCelebrate
styleAndCelebrate(`'ef7c8e'`, `'fae8e0'`, `'30px'`, `'You made it!'`, `'champions'`)


// Failed Test 1: Not logging the consoleStyler() variables
// Passed Test 2: successfully logged celebrateStyler() variables
// Failed Test 3: Not calling consoleStyler() and celebrateStyler()
// Failed Test 4: Not calling styleAndCelebrate()