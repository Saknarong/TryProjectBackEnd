/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, { Component } from 'react';
import { Platform, StyleSheet, Text, View, ScrollView, Button, Image, ImageBackground } from 'react-native';


const instructions = Platform.select({
  ios: 'Press Cmd+R to reload,\n' + 'Cmd+D or shake for dev menu',
  android:
    'Double tap R on your keyboard to reload,\n' +
    'Shake or press menu button for dev menu',
});


export default class SelectPageFemale extends Component {
  render() {
    return (
      <ScrollView>

        <ImageBackground
          source={require('./img/bg.png')}
          style={{ height: '100%' }}>


          <View style={{ flex: 1, flexDirection: 'row', height: 2000 }}>

            <View style={{ flex: 0.05 }}>
            </View>

            <View style={{ flex: 0.9, backgroundColor: '', marginBottom: 20 }}>
              <View style={{ flex: 0.1, flexDirection: 'column', backgroundColor: '' }}>
                <Text style={{ fontSize: 20, textAlign: 'center', marginTop: 90, color: 'white', fontWeight: 'bold' }}>Select Your Body Shape </Text>
              </View>

              <View style={{ flex: 0.9, backgroundColor: 'white', borderRadius: 10 }}>
                <View style={{ flex: 1, flexDirection: 'row' }}>
                  <View style={{ flex: 0.5, flexDirection: 'row', backgroundColor: '', margin: 15, marginRight: 7.5 }}>
                    {/* //Green1 */}
                    <View style={{ flex: 1, flexDirection: 'column' }}>
                      {/* //Col1Row1 */}
                      <View style={{ flex: 0.16, backgroundColor: '#F9F9F9', marginBottom: 15, borderRadius: 10 }}>
                        <Image
                          style={{ flex: 1, height: 300, marginTop: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                        />
                        <Text style={{ color: 'gray', fontWeight: 'bold', textAlign: 'center', marginBottom: 15, marginTop: 10 }}>Test</Text>
                      </View>

                      <View style={{ flex: 0.16, backgroundColor: '#F9F9F9', marginBottom: 15, borderRadius: 10 }}>
                        <Image
                          style={{ flex: 1, height: 300, marginTop: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                        />
                        <Text style={{ color: 'gray', fontWeight: 'bold', textAlign: 'center', marginBottom: 15, marginTop: 10 }}>Test</Text>
                      </View>

                      <View style={{ flex: 0.16, backgroundColor: '#F9F9F9', marginBottom: 15, borderRadius: 10 }}>
                        <Image
                          style={{ flex: 1, height: 300, marginTop: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                        />
                        <Text style={{ color: 'gray', fontWeight: 'bold', textAlign: 'center', marginBottom: 15, marginTop: 10 }}>Test</Text>
                      </View>

                      <View style={{ flex: 0.16, backgroundColor: '#F9F9F9', marginBottom: 15, borderRadius: 10 }}>
                        <Image
                          style={{ flex: 1, height: 300, marginTop: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                        />
                        <Text style={{ color: 'gray', fontWeight: 'bold', textAlign: 'center', marginBottom: 15, marginTop: 10 }}>Test</Text>
                      </View>

                      <View style={{ flex: 0.16, backgroundColor: '#F9F9F9', marginBottom: 15, borderRadius: 10 }}>
                        <Image
                          style={{ flex: 1, height: 300, marginTop: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                        />
                        <Text style={{ color: 'gray', fontWeight: 'bold', textAlign: 'center', marginBottom: 15, marginTop: 10 }}>Test</Text>
                      </View>

                      <View style={{ flex: 0.16, backgroundColor: '#F9F9F9', marginBottom: 15, borderRadius: 10 }}>
                        <Image
                          style={{ flex: 1, height: 300, marginTop: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                        />
                        <Text style={{ color: 'gray', fontWeight: 'bold', textAlign: 'center', marginBottom: 15, marginTop: 10 }}>Test</Text>
                      </View>

                    </View>

                  </View>

                  <View style={{ flex: 0.5, flexDirection: 'row', backgroundColor: '', margin: 15, marginLeft: 7.5 }}>
                    {/* //Green2 */}

                    <View style={{ flex: 1, flexDirection: 'column' }}>
                      {/* //Col1Row1 */}
                      <View style={{ flex: 0.16, backgroundColor: '#F9F9F9', marginBottom: 15, borderRadius: 10 }}>
                        <Image
                          style={{ flex: 1, height: 300, marginTop: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                        />
                        <Text style={{ color: 'gray', fontWeight: 'bold', textAlign: 'center', marginBottom: 15, marginTop: 10 }}>Test</Text>
                      </View>

                      <View style={{ flex: 0.16, backgroundColor: '#F9F9F9', marginBottom: 15, borderRadius: 10 }}>
                        <Image
                          style={{ flex: 1, height: 300, marginTop: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                        />
                        <Text style={{ color: 'gray', fontWeight: 'bold', textAlign: 'center', marginBottom: 15, marginTop: 10 }}>Test</Text>
                      </View>

                      <View style={{ flex: 0.16, backgroundColor: '#F9F9F9', marginBottom: 15, borderRadius: 10 }}>
                        <Image
                          style={{ flex: 1, height: 300, marginTop: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                        />
                        <Text style={{ color: 'gray', fontWeight: 'bold', textAlign: 'center', marginBottom: 15, marginTop: 10 }}>Test</Text>
                      </View>

                      <View style={{ flex: 0.16, backgroundColor: '#F9F9F9', marginBottom: 15, borderRadius: 10 }}>
                        <Image
                          style={{ flex: 1, height: 300, marginTop: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                        />
                        <Text style={{ color: 'gray', fontWeight: 'bold', textAlign: 'center', marginBottom: 15, marginTop: 10 }}>Test</Text>
                      </View>

                      <View style={{ flex: 0.16, backgroundColor: '#F9F9F9', marginBottom: 15, borderRadius: 10 }}>
                        <Image
                          style={{ flex: 1, height: 300, marginTop: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                        />
                        <Text style={{ color: 'gray', fontWeight: 'bold', textAlign: 'center', marginBottom: 15, marginTop: 10 }}>Test</Text>
                      </View>

                      <View style={{ flex: 0.16, backgroundColor: '#F9F9F9', marginBottom: 15, borderRadius: 10 }}>
                        <Image
                          style={{ flex: 1, height: 300, marginTop: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                        />
                        <Text style={{ color: 'gray', fontWeight: 'bold', textAlign: 'center', marginBottom: 15, marginTop: 10 }}>Test</Text>
                      </View>

                    </View>

                  </View>


                </View>




              </View>


              <View style={{ flex: 0.1 }}>
                <Text style={{ fontSize: 20, textAlign: 'center', marginTop: 90, color: 'gray', fontWeight: 'bold' }}>Select Your Skin Color
              </Text>
              </View>

              <View style={{ flex: 0.2, backgroundColor: 'white', borderRadius: 10 }}>

                <View style={{ flex: 2, flexDirection: 'column' }}>
                  <View style={{ flex: 1, flexDirection: 'column' }}>
                    <View style={{ flex: 3, flexDirection: 'row', marginTop: 30, marginHorizontal: 10 }}>
                      <View style={{ flex: 1, flexDirection: 'row' }} >
                        <Image
                          style={{ height: 100, width: 100, borderRadius: 100 / 2, margin: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                          onPress={{source: '/'}}
                        />
                      </View>

                      <View style={{ flex: 1, flexDirection: 'row' }} >
                        <Image
                          style={{ height: 100, width: 100, borderRadius: 100 / 2, margin: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                          onPress={{source: '/'}}
                        />
                      </View>

                      <View style={{ flex: 1, flexDirection: 'row' }} >
                        <Image
                          style={{ height: 100, width: 100, borderRadius: 100 / 2, margin: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                          onPress={{source: '/'}}
                        />
                      </View>
                    </View>

                  </View>

                  <View style={{ flex: 1, flexDirection: 'column' }}>
                    <View style={{ flex: 3, flexDirection: 'row', marginHorizontal: 10, marginBottom: 30 }}>
                      <View style={{ flex: 1, flexDirection: 'row' }} >
                        <Image
                          style={{ height: 100, width: 100, borderRadius: 100 / 2, margin: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png'}}
                          onPress={{source: '/'}}
                          />
                      </View>

                      <View style={{ flex: 1, flexDirection: 'row' }} >
                        <Image
                          style={{ height: 100, width: 100, borderRadius: 100 / 2, margin: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                          onPress={{source: '/'}}
                        />
                      </View>

                      <View style={{ flex: 1, flexDirection: 'row' }} >
                        <Image
                          style={{ height: 100, width: 100, borderRadius: 100 / 2, margin: 10 }}
                          source={{ uri: 'https://facebook.github.io/react-native/docs/assets/favicon.png' }}
                          onPress={{source: '/'}}
                        />
                      </View>
                    </View>

                  </View>


                </View>




              </View>

              <View style={{ flex: 0.1, marginTop: 30, flexDirection: 'row' }}>
                <View style={{ flex: 0.5, margin: 15 }}>
                  <Button
                    onPress={{ source: '/' }}
                    title="< Back"
                    color="#ACACAC"
                    borderRadius="10"
                  />
                </View>
                <View style={{ flex: 0.5, margin: 15 }}>
                  <Button
                    onPress={{ source: '/' }}
                    title="Next >"
                    color="#949494"
                    borderRadius="10"
                  />
                </View>
              </View>
            </View>



            <View style={{ flex: 0.05 }}>
            </View>

          </View>

        </ImageBackground>
      </ScrollView>
    );
  }
}



const styles = StyleSheet.create({
  shadow: {
    shadowOffset: { width: 10, height: 10 },
    shadowColor: 'black',
    shadowOpacity: 1.0
  }
});
// const styles = StyleSheet.create({
//   container: {
//     flex: 1,
//     backgroundColor: 'violet',
//   },
  //   welcome: {
  //     fontSize: 20,
  //     textAlign: 'center',
  //     margin: 10,
  //   },
  //   instructions: {
  //     textAlign: 'center',
  //     color: '#333333',
  //     marginBottom: 5,
  //   },
  //
//});   
