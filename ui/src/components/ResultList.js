import React, { Component } from 'react';
import axios from 'axios';
import ResultRow from './ResultRow';

const list = [
  {
    "id":2,
    "query":"AGTT",
    "processed":"True",
    "result":{
      "protein":{"name":"Mollivirus sibericum isolate P1084-T","code":"NC_027867"},
      "location":360,
      "created_at":"2019-06-10T03:51:53.926134Z","updated_at":"2019-06-10T03:51:53.926197Z"},
    "created_at":"2019-06-10T03:51:53.819265Z",
    "updated_at":"2019-06-10T03:51:53.928022Z"
  },
  {
    "id":3,
    "query":"AGTTAGC",
    "processed":"True",
    "result":{
      "protein":{"name":"Paramecium bursaria Chlorella virus AR158","code":"NC_009899"},
      "location":42244,
      "created_at":"2019-06-10T03:52:06.811780Z",
      "updated_at":"2019-06-10T03:52:06.811815Z"
    },
    "created_at":"2019-06-10T03:52:06.665978Z",
    "updated_at":"2019-06-10T03:52:06.813361Z"
  },
  {
    "id":5,
    "query":"GATGAT",
    "processed":"False",
    "result":null,
    "created_at":"2019-06-10T05:11:36.651364Z",
    "updated_at":"2019-06-10T05:11:36.651433Z"
  }
];

export default class ResultList extends Component {
  constructor(props) {
    super(props);
    this.state = {searches: list};
  }
  componentDidMount(){
    axios.get('http://localhost:8000/v1/searches/?format=json', { withCredentials: true })
    .then(response => {
      console.log('Got response', response);
      this.setState({ searches: response.data });
    })
    .catch(function (error) {
      console.log(error);
    })
  }
  tabRow(){
    return this.state.searches.map(function(object, i){
      return <ResultRow obj={object} key={i} />;
    });
  }

  render() {
    return (
      <div className="container">
          <table className="table table-striped">
            <thead>
              <tr>
                <td>DNA Sequence</td>
                <td>Status</td>
                <td>Result</td>
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
