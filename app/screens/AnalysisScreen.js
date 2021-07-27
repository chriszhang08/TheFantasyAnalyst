import React, { Component } from "react";
import { View, Text, ActivityIndicator } from "react-native";
import { Form } from "/Users/chris/DoneWithIt/app/form.js";

class AnalysisScreen extends React.Component {
  constructor(props) {
    super(props);
    console.log(props.navigation.state.params.home[7]);
    this.state = { isLoading: true };
  }

  componentDidMount() {
    console.log("componentDidMount");
    return fetch("http://127.0.0.1:3000/analyze/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        homeName: this.props.navigation.state.params.homeName,
        homeScore: this.props.navigation.state.params.home,
        awayName: this.props.navigation.state.params.awayName,
        awayScore: this.props.navigation.state.params.away,
      }),
    })
      .then((response) => response.json())
      .then((responseJson) => {
        this.setState(
          {
            isLoading: false,
            dataSource: responseJson.results,
          },
          function () {}
        );
      })
      .catch((error) => {
        console.error(error);
      });
  }

  render() {
    console.log("Test");
    console.log(this.state.dataSource);
    if (this.state.isLoading) {
      return (
        <View style={{ flex: 1, padding: 20 }}>
          <ActivityIndicator />
        </View>
      );
    }
    return (
      <View style={{ flex: 1, paddingTop: 20 }}>
        <Text>Optimized lineup: </Text>
        {this.state.dataSource[0].lineup.map((item, key) => (
          <Text key={key}> {item} </Text>
        ))}
        <Text>Total points scored: {this.state.dataSource[1].pointsFor}</Text>
        <Text>Adjusted combined record (W-L-T)</Text>
        <Text>
          {this.state.dataSource[2].adjRecord[0]}-
          {this.state.dataSource[2].adjRecord[1]}-
          {this.state.dataSource[2].adjRecord[2]}
        </Text>
        <Text>Adjusted and optimized combined record</Text>
        <Text>
          {this.state.dataSource[3].adjOptRecord[0]}-
          {this.state.dataSource[3].adjOptRecord[1]}-
          {this.state.dataSource[3].adjOptRecord[2]}
        </Text>
        <Text>Adjusted head to head record against specified team(W-L-T)</Text>
        <Text>
          {this.state.dataSource[4].adjh2hRecord[0]}-
          {this.state.dataSource[4].adjh2hRecord[1]}-
          {this.state.dataSource[4].adjh2hRecord[2]}
        </Text>
        <Text>
          Average Points Scored: {this.state.dataSource[5].avgPointsPWeek}
        </Text>
        <Text>
          Median Points Scored: {this.state.dataSource[8].medPointsPWeek}
        </Text>
        <Text>Best Coach Award: {this.state.dataSource[6].bestCoach}</Text>
        <Text>Worst Coach Award: {this.state.dataSource[7].worstCoach}</Text>
      </View>
    );
  }
}

export default AnalysisScreen;
