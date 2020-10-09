let express = require("express")
let ourApp = express()
// enabling the feature to get access to post data
ourApp.use(express.urlencoded({extended: false}))

// Tell server to listen to incoming requests
// This function is for what to do on get requests
ourApp.get('/', function (req, res) {
    res.send(`
    <form action="/answer" method="POST">
        <p>What color is the sky on a bright and sunny day?</p>
        <label for="color">Sky color:</label><br>
        <input type="text" id="color" name="color" value=""><br>
        <input type="submit" value="Submit">
    </form> 
    `);
})

ourApp.post('/answer', function(req, res){
    if(req.body.color == "blue"){
        res.send(`
            <p>Yes that is the correct answer.</p>
            <a href="/">Back to home page</a>
        `)
    } else {
        res.send(`
            <p>No this is not the correct answer.</p>
            <a href="/">Back to home page</a>
        `)
    }
})

ourApp.get('/answer', function(req, res){
    res.send("Are you lost? There is nothing to see here.")
})
ourApp.listen(3000)

