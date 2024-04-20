import Typewriter from "components/Typewriter";
import 'bootstrap/dist/css/bootstrap.min.css'; // Import Bootstrap CSS

const Icons = () => {

  return (
    <div className='bg-light'>
      <div className='bg-warning mx-auto pl-9 '>
          <h1 className='font-weight-bold '>NLP.AI: <Typewriter text="Revolutionizing NLP with Transformers" delay={200} infinite />
</h1>
</div>
<form>

<div class="form-group w-50 mx-auto pt-9 text-center ">
<h1 className='text-center mb-5 '>Text Generation</h1>

    <textarea placeholder='Enter prompt...' class="form-control" id="exampleFormControlTextarea1" rows="1"></textarea>

  </div>
  <div class="col-md-12 text-center">
            <button type="button" class="btn btn-warning" >Generate</button>
        </div></form>
</div>
  );
};

export default Icons;
