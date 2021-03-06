import axios from 'axios';
import { toast } from 'react-toastify';
import React, { Component } from 'react';
import SearchForm from './components/SearchForm';
import ResultList from './components/ResultList';

import './App.css';
import '../node_modules/react-toastify/dist/ReactToastify.min.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

toast.configure({
  autoClose: 3000,
  draggable: false
});

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
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
          <a className="navbar-brand" href="#">Protein Searcher</a>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <SearchForm></SearchForm>
            <form className="form-inline">
              <button
                className="btn btn-outline-secondary my-2 my-sm-0 ml-2"
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
