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
        <div style={{marginTop: 50}}>
          <h3>Search Proteins</h3>
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <label>DNA sequence:</label>
              <input
                type="text"
                className="form-control"
                value={this.state.query}
                onChange={this.onChangeQuery}
              />
            </div>
            <div className="form-group">
              <input type="submit" value="Go!" className="btn btn-primary"/>
            </div>
          </form>
        </div>
      )
    }
}
