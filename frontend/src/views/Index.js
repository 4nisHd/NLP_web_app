import 'bootstrap/dist/css/bootstrap.css';
import Typewriter from 'components/Typewriter';
import { useState } from 'react';
import axios from 'axios';
import Wordwriter from 'components/Wordwriter';
const Index = () => {
  const [paragraph, setParagraph] = useState('');

  const handleClick = async (button) => {
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/get-paragraph', { buttonClick: button });
      setParagraph(response.data.paragraph);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className='bg-light'>
      <div className='bg-warning mx-auto pl-9'>
          <h1 className='font-weight-bold'>NLP.AI: <Typewriter text="Revolutionizing NLP with Transformers" delay={200} infinite />
</h1>
</div>
<form>

<div class="form-group w-50 mx-auto pt-9 text-center ">
<h1 className='text-center mb-5'>Text Summerization</h1>

    <textarea placeholder='Enter text...' class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>

  </div>
  <div class="col-md-12 text-center">
            <button type="button" class="btn btn-warning" onClick={() => handleClick('button1')}>Summarize</button>
            <p><Wordwriter text={paragraph} delay={150} /></p>
        </div></form>
</div>
  );
};

export default Index;
