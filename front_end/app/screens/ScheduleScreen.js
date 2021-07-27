// keyboard shortcut rsf
import React from "react";
import { StyleSheet, View } from "react-native";
import { ScrollView } from "react-native-gesture-handler";

import colors from "../config/colors";
import FlatButton from "/Users/chris/DoneWithIt/app/button.js";

function ScheduleScreen({ navigation, route }) {
  const pressHandler = () => {
    navigation.navigate("ImportWeekScreen", { title: "Abhi", rating: 5 });
  };
  console.log(navigation);
  return (
    <ScrollView style={styles.container}>
      <FlatButton text="Week 1 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 2 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 3 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 4 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 5 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 6 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 7 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 8 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 9 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 10 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 11 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 12 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 13 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 14 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 15 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 16 Matchups" onPress={pressHandler} />
      <FlatButton text="Week 17 Matchups" onPress={pressHandler} />
    </ScrollView>
  );
}
// keyboard shortcut rnss
const styles = StyleSheet.create({
  container: {
    backgroundColor: colors.blue,
    flex: 1,
  },
});

export default ScheduleScreen;
