const express=require('express');
const app=express();
const PORT= process.env.PORT || 5000;
const mongoose = require('mongoose');
//jsonparsing
app.use(express.json());
//routes
app.use('/api/auth',require('./routes/auth'));

mongoose.connect('mongodb://localhost:27017/nlpdb',{
    useNewUrlParser: true,
    useUnifiedTopology: true,
})
.then(()=> console.log('MongoDB connected'))
.catch(err => console.log(err))
//startserver
app.listen(PORT,()=> console.log(`Server running on port ${PORT}`));
