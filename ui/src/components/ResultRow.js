import React, { Component } from 'react';

class ResultRow extends Component {
  render() {
    return (
      <tr>
        <td>
          {this.props.obj.query}
        </td>
        <td>
          {this.props.obj.processed ? 'Done' : 'Pending'}
        </td>
        <td>
          {this.props.obj.result && this.props.obj.result.location > -1 ?
            `Found in ${this.props.obj.result.protein.code}: ${this.props.obj.result.protein.name} at ${this.props.obj.result.location}` : 
            'No matches found'
          }
        </td>
      </tr>
    );
  }
}

export default ResultRow;
