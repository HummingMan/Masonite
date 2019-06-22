import React, { Component } from 'react';
import axios from 'axios';

export default class App extends Component {
  state = {
    toppage: '',
  }

  getToppage=()=>{
    axios.get('/my-site/api/get_toppage')
    .then(response=>{
      this.setState({
        toppage: response.toppage,
      })
    })
    .catch(e=>{
      console.error('通信エラー');
    })
  }

  componentDidMount(){
    this.getToppage();
  }

  render(){
    return(
      <div>
        {this.state.toppage}
      </div>
    );
  }
}