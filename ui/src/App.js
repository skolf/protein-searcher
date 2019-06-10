import React, { Component } from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import SearchForm from './components/SearchForm';
import ResultList from './components/ResultList';
import './App.css';

import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

class App extends Component {
  render() {
    return (
      <Router>
        <div className="container">
          <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <a className="navbar-brand">Protein Searcher</a>
            <div className="collapse navbar-collapse" id="navbarSupportedContent">
              <ul className="navbar-nav mr-auto">
                <li className="nav-item"><Link to={'/search'} className="nav-link">Search</Link></li>
                <li className="nav-item"><Link to={'/list'} className="nav-link">List</Link></li>
              </ul>
              <hr />
            </div>
          </nav>
          <Switch>
              <Route exact path='/search' component={ SearchForm } />
              <Route path='/list' component={ ResultList } />
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
