import axios from 'axios';
import React, { Component } from 'react';
import SearchForm from './components/SearchForm';
import ResultList from './components/ResultList';

import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.listSearches = this.listSearches.bind(this);

    this.state = {searches: []};
  }

  componentDidMount(){
    this.listSearches();
  }

  listSearches(){
    axios.get('http://localhost:8000/v1/searches/?format=json', { withCredentials: true })
      .then(response => {
        this.setState({ searches: response.data });
      })
      .catch(function (error) {
        console.log(error);
      })
  }

  render() {
    return (
      <div className="container">
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
          <a className="navbar-brand" href="#">Protein Searcher</a>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <SearchForm></SearchForm>
            <form className="form-inline">
              <button
                className="btn btn-outline-secondary my-2 my-sm-0"
                type="button"
                onClick={ this.listSearches }
              >
                Refresh
              </button>
            </form>
          </div>
        </nav>
        <ResultList searches={this.state.searches}></ResultList>
      </div>
    );
  }
}

export default App;
