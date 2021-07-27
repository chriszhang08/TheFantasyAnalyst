// keyboard shortcut rsf
import * as React from "react";
import {
  Image,
  StyleSheet,
  View,
  TextInput,
  Text,
  SafeAreaView,
  Button,
} from "react-native";

import colors from "../config/colors";

function ImportWeekScreen({ navigation }) {
  const [name, setName] = React.useState("Chris Zhang");
  const [hScore, sethScore] = React.useState(0);
  const [hqbS, sethqbS] = React.useState(0);
  const [hrb1S, sethrb1S] = React.useState(0);
  const [hrb2S, sethrb2S] = React.useState(0);
  const [hwr1S, sethwr1S] = React.useState(0);
  const [hwr2S, sethwr2S] = React.useState(0);
  const [hteS, sethteS] = React.useState(0);
  const [hflexS, sethflexS] = React.useState(0);
  const [hdstS, sethdstS] = React.useState(0);
  const [hkS, sethkS] = React.useState(0);
  const [hb1S, sethb1S] = React.useState(0);
  const [hb2S, sethb2S] = React.useState(0);
  const [hb3S, sethb3S] = React.useState(0);
  const [hb4S, sethb4S] = React.useState(0);
  const [hb5S, sethb5S] = React.useState(0);
  const [hb6S, sethb6S] = React.useState(0);
  const [aScore, setaScore] = React.useState(0);
  const [aqbS, setaqbS] = React.useState(0);
  const [arb1S, setarb1S] = React.useState(0);
  const [arb2S, setarb2S] = React.useState(0);
  const [awr1S, setawr1S] = React.useState(0);
  const [awr2S, setawr2S] = React.useState(0);
  const [ateS, setateS] = React.useState(0);
  const [aflexS, setaflexS] = React.useState(0);
  const [adstS, setadstS] = React.useState(0);
  const [akS, setakS] = React.useState(0);
  const [ab1S, setab1S] = React.useState(0);
  const [ab2S, setab2S] = React.useState(0);
  const [ab3S, setab3S] = React.useState(0);
  const [ab4S, setab4S] = React.useState(0);
  const [ab5S, setab5S] = React.useState(0);
  const [ab6S, setab6S] = React.useState(0);

  //const { rating } = route.params;
  return (
    <SafeAreaView style={styles.submit}>
      <View style={styles.container}>
        {/* TEAM 2 __________________________ */}
        <View style={styles.team1}>
          <Text>Home Team: </Text>
          <TextInput
            keyboardType="numeric"
            style={styles.input}
            placeholder="Score"
            onChangeText={(val) => sethScore(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="QB"
            onChangeText={(val) => sethqbS(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="RB1"
            onChangeText={(val) => sethrb1S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="RB2"
            onChangeText={(val) => sethrb2S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="WR1"
            onChangeText={(val) => sethwr1S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="WR2"
            onChangeText={(val) => sethwr2S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="TE"
            onChangeText={(val) => sethteS(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="Flex"
            onChangeText={(val) => sethflexS(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="D/ST"
            onChangeText={(val) => sethdstS(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="K"
            onChangeText={(val) => sethkS(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="Bench1"
            onChangeText={(val) => sethb1S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="Bench2"
            onChangeText={(val) => sethb2S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="Bench3"
            onChangeText={(val) => sethb3S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="Bench4"
            onChangeText={(val) => sethb4S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="Bench5"
            onChangeText={(val) => sethb5S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="Bench6"
            onChangeText={(val) => sethb6S(val)}
          />
        </View>
        {/* TEAM 2 __________________________ */}
        <View style={styles.team2}>
          <Text>Away Team: </Text>
          <TextInput
            keyboardType="numeric"
            style={styles.input}
            placeholder="Score"
            onChangeText={(val) => setaScore(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="QB"
            onChangeText={(val) => setaqbS(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="RB1"
            onChangeText={(val) => setarb1S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="RB2"
            onChangeText={(val) => setarb2S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="WR1"
            onChangeText={(val) => setawr1S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="WR2"
            onChangeText={(val) => setawr2S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="TE"
            onChangeText={(val) => setateS(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="Flex"
            onChangeText={(val) => setaflexS(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="D/ST"
            onChangeText={(val) => setadstS(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="K"
            onChangeText={(val) => setakS(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="Bench1"
            onChangeText={(val) => setab1S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="Bench2"
            onChangeText={(val) => setab2S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="Bench3"
            onChangeText={(val) => setab3S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="Bench4"
            onChangeText={(val) => setab4S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="Bench5"
            onChangeText={(val) => setab5S(val)}
          />
          <TextInput
            keyboardType="default"
            style={styles.input}
            placeholder="Bench6"
            onChangeText={(val) => setab6S(val)}
          />
        </View>
      </View>
      <Button
        title="Submit"
        onPress={() => {
          // Pass and merge params back to home screen
          navigation.navigate(
            "AnalysisScreen",
            {
              homeName: "TeamPackingSteel",
              home: {
                qb: hqbS,
                rb1: hrb1S,
                rb2: hrb2S,
                wr1: hwr1S,
                wr2: hwr2S,
                te: hteS,
                flex: hflexS,
                dst: hdstS,
                k: hkS,
                b1: hb1S,
                b2: hb2S,
                b3: hb3S,
                b4: hb4S,
                b5: hb5S,
                b6: hb6S,
              },
              awayName: "ZhangsGang",
              away: {
                qb: aqbS,
                rb1: arb1S,
                rb2: arb2S,
                wr1: awr1S,
                wr2: awr2S,
                te: ateS,
                flex: aflexS,
                dst: adstS,
                k: akS,
                b1: ab1S,
                b2: ab2S,
                b3: ab3S,
                b4: ab4S,
                b5: ab5S,
                b6: ab6S,
              },
            },
            true
          );
        }}
      />
    </SafeAreaView>
  );
}

// keyboard shortcut rnss
const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: "row",
    justifyContent: "space-around",
  },
  input: {
    borderWidth: 1,
    borderColor: "#777",
    padding: 6,
    margin: 6,
    width: 180,
  },
  submit: {
    backgroundColor: colors.white,
    flex: 1,
    flexDirection: "column",
    justifyContent: "space-between",
  },
  team1: {
    alignItems: "center",
  },
  team2: {
    alignItems: "center",
  },
});

export default ImportWeekScreen;
