import Typewriter from "components/Typewriter";
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS
import { useState } from "react";
import axios from "axios";
const Icons = () => {
  const [generatedText, setGeneratedText] = useState('');
  const [textData, setTextData] = useState(''); // State to store text data from the textarea

  const handleClick = async (button) => {
    try {
      console.log('Current Text Data:', textData);
      const last50Characters = textData.slice(-50);
      const response = await axios.post(
        'http://127.0.0.1:5000/api/text-generation/',
        { buttonClick: button, textData:last50Characters  },
        { headers: { 'Content-Type': 'application/json' } } // Specify Content-Type header
      );
      const generatedText = JSON.stringify(response.data.generated_text);
      const jsonArray = JSON.parse(generatedText);
      const genT = jsonArray[0].generated_text;

      setGeneratedText(genT); // Update generatedText with the string value
      setTextData(prevTextData => prevTextData + genT);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleTextareaChange = (event) => {
    setTextData(event.target.value); // Update the text data state as the user types in the textarea
  };

  return (
    <div className='bg-light'>
      <div className='bg-warning mx-auto pl-9 '>
        <h1 className='font-weight-bold '>
          ARNLP:  الذكاء الصناعي في خدمة اللغة العربية
        </h1>
      </div>
      <form>
        <div className="form-group mx-auto w-50 pt-9 text-center">
          <h1 className='text-center mb-5'>انشاء نص</h1>
          <textarea
            placeholder='أدخل نص...'
            className="form-control"
            value={textData}
            onChange={handleTextareaChange}
            id="exampleFormControlTextarea1"
            rows="7"
            style={{
              borderRadius: '10px', // Rounded edges
              backgroundColor: '#ffffff', // Gray background color
              borderColor: '#ffffff', // Gray border color
              boxShadow: 'inset 0px 0px 5px 1px rgba(0, 0, 0, 0.2)', // Inner shadow
            }}
          ></textarea>
        </div>
        <div className="col-md-12 text-center">
          <button
            type="button"
            className="btn btn-warning"
            onClick={() => handleClick("generate")}
          >
            أكمل النص
          </button>
        </div>
      </form>
    </div>
  );
};

export default Icons;
