import React, { Component } from 'react';
import axios from 'axios';

export default class SearchForm extends Component {

    constructor(props) {
      super(props);
      this.onChangeQuery = this.onChangeQuery.bind(this);
      this.onSubmit = this.onSubmit.bind(this);

      this.state = {
        query: ''
      }
    }
    onChangeQuery(e) {
      this.setState({
        query: e.target.value
      });
    }
    onSubmit(e) {
      e.preventDefault();
      const data = {query: this.state.query};
      axios.post('http://localhost:8000/v1/searches/', data, {withCredentials: true})
        .then(res => console.log(res.data));

      this.setState({
        query: ''
      });
    }

    render() {
      return (
        <form className="form-inline my-2 my-lg-0" onSubmit={this.onSubmit}>
          <input
            type="search"
            className="form-control mr-sm-2"
            value={this.state.query}
            onChange={this.onChangeQuery}
            placeholder="DNA sequence"
            aria-label="Search"
          />
          <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
      )
    }
}
