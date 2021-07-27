import React from "react";
import { StyleSheet, Text, View, TouchableOpacity } from "react-native";
import colors from "./config/colors";

export default function FlatButton({ text, onPress }) {
  return (
    <TouchableOpacity onPress={onPress}>
      <View style={styles.button}>
        <Text style={styles.buttonText}>{text}</Text>
      </View>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  button: {
    borderRadius: 32,
    paddingVertical: 50,
    paddingHorizontal: 80,
    margin: 6,
    backgroundColor: colors.silver,
  },
  buttonText: {
    color: "white",
    fontWeight: "bold",
    textTransform: "uppercase",
    fontSize: 22,
    textAlign: "center",
  },
});
