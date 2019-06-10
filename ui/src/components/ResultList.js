import React, { Component } from 'react';
import ResultRow from './ResultRow';

export default class ResultList extends Component {
  tabRow(){
    return this.props.searches.map(function(object, i){
      return <ResultRow obj={object} key={i} />;
    });
  }

  render() {
    return (
      <div className="container">
          <table className="table table-striped">
            <thead>
              <tr>
                <th>DNA Sequence</th>
                <th>Status</th>
                <th>Result</th>
              </tr>
            </thead>
            <tbody>
              {this.tabRow()}
            </tbody>
          </table>
      </div>
    );
  }
}
