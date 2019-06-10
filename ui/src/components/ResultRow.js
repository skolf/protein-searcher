import React, { Component } from 'react';

class ResultRow extends Component {
  constructor(props) {
    super(props);
    this.resultString = this.resultString.bind(this);
  }

  resultString() {
    if (this.props.obj.result && this.props.obj.result.location > -1) {
      return `Found in ${this.props.obj.result.protein.code}:
        ${this.props.obj.result.protein.name} at ${this.props.obj.result.location}`
    } else {
      return 'No matches found';
    }
  }

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
          {this.resultString()}
        </td>
      </tr>
    );
  }
}

export default ResultRow;
