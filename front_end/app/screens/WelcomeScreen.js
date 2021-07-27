import React from "react";
import { ImageBackground, StyleSheet, Text, View } from "react-native";
import FlatButton from "/Users/chris/DoneWithIt/app/button.js";

function WelcomeScreen({ navigation }) {
  const pressHandler = () => {
    navigation.navigate("ScheduleScreen", { test: 57, team: "LemonDonkey" });
    //navigation.push("ScheduleScreen");
  };
  const pressHandler2 = () => {
    navigation.navigate("AnalysisScreen");
    //navigation.push("ScheduleScreen");
  };

  return (
    <ImageBackground
      style={styles.background}
      source={require("/Users/chris/DoneWithIt/app/assets/lionspichomepage.jpeg")}
    >
      <View style={styles.logoContainer}>
        <Text style={styles.baseText}>The Fantasy Professor</Text>
      </View>

      <View style={styles.buttonContainer}>
        <FlatButton text="Import Fantasy Teams" onPress={pressHandler} />
      </View>
      <View style={styles.buttonContainer2}>
        <FlatButton text="View Analysis" onPress={pressHandler2} />
      </View>
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  background: {
    flex: 1,
    justifyContent: "flex-end",
    alignItems: "center",
  },
  baseText: {
    fontFamily: "Papyrus",
    fontSize: 35,
    color: "#ffffff",
    // backgroundColor: "#000",
  },
  logoContainer: {
    position: "absolute",
    top: 40,
    alignItems: "center",
  },
  buttonContainer: {
    position: "absolute",
    bottom: 40,
    alignItems: "center",
  },
  buttonContainer2: {
    position: "absolute",
    bottom: 200,
    alignItems: "center",
  },
});

export default WelcomeScreen;
