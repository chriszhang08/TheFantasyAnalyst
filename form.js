import React from "react";
import {
  StyleSheet,
  TouchableOpactiy,
  Text,
  TextInput,
  View,
  Touchable,
  TouchableOpacity,
} from "react-native";
import colors from "./config/colors";

export const Form = () => {
  const handleSubmit = (event) => {
    event.preventDefault();
  };
  return (
    <TextInput keyboardType="default" style={styles.input} placeholder="Test" />
  );
};

const styles = StyleSheet.create({
  input: {
    borderWidth: 1,
    borderColor: "#777",
    padding: 6,
    margin: 6,
    width: 180,
  },
});
