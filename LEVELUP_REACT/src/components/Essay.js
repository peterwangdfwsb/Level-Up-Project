import React from 'react';
import './Essay.css';


class Essay extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        value: ''
      };
  
      this.handleChange = this.handleChange.bind(this);
      //this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleChange(event) {
      this.setState({value: event.target.value});
    }
  
    //handleSubmit(event) {
      //alert('An essay was submitted: ' + this.state.value);
      //event.preventDefault();
    //}

  
    render() {
      return (
        <div className='form_tag'>
        <form onSubmit={this.handleSubmit}>
         <textarea placeholder="Enter your sentence" value={this.state.value} onChange={this.handleChange} rows="15" cols='50'/>
        </form>
        </div>
      );
    }
  }

  export default Essay;