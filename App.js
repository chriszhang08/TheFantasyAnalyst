import { StatusBar } from "expo-status-bar";
import React from "react";
import "react-native-gesture-handler";
import {
  StyleSheet,
  Text,
  View,
  Dimensions,
  TouchableHighlight,
  Alert,
  Image,
  Button,
  Platform,
  SafeAreaView,
} from "react-native";
import {
  useDimensions,
  useDeviceOrientation,
} from "@react-native-community/hooks";
import Navigator from "./routes/homeStack";
import { NavigationContainer } from "@react-navigation/native";
import WelcomeScreen from "./app/screens/WelcomeScreen.js";
import ScheduleScreen from "./app/screens/ScheduleScreen.js";
import ImportWeekScreen from "./app/screens/ImportWeekScreen.js";

export default function App() {
  return <Navigator />;
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    paddingTop: Platform.OS === "android" ? StatusBar.currentHeight : 0,
  },
});
