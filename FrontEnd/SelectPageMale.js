import React, { Component } from 'react';
import { StyleSheet, Text, View, ScrollView, Image, ImageBackground, TouchableOpacity, FlatList, Button } from 'react-native';
import axios from 'axios';



export default class SelectPageMale extends Component {

  state = {
    data: []
  }


  getShape = async () => {
    const resp = await axios.get('http://3.84.76.238:8000/menShape/')
    console.log('shape is serving....')
    let data = resp.data.map(value => {
      return value
    })
    this.setState({ data })

  }
  componentDidMount = async () => {
    await this.getShape()
    console.log('serving done!');
  }


  // constructor() {
  //   super()
  //   this.state = {
  //     dataSource: []
  //   }
  // }

  // renderItem = ({ item }) => {
  //   return (
  //     <TouchableOpacity>
  //       <Text>{item.skinColorCode}</Text>
  //     </TouchableOpacity>
  //   )


  // }

  // componentWillMount() {
  //   const url = '3.84.76.238/skinColorManagement'
  //   fetch(url)
  //     .then((response) => response.json())
  //     .then((responseJson) => {
  //       this.setState({
  //         dataSource: responseJson.skinColorCode
  //       })
  //     })
  //     .catch((error) => {
  //       console.log(error)
  //     })
  // }

  render() {

    return (
      <ScrollView>

        <ImageBackground
          source={require('./android/app/img/bg.png')}
          style={styles.ImageBackgroundStyle}>
          <View>
            <Text style={styles.TextStyle}>Select Your Body Shape </Text>
          </View>
          <View style={styles.Container}>
            <View style={styles.Container}>
              {this.state.data.map((val, index) => (

                <View key={index}>
                  {console.log(val.shapePictureUrl)}
                  {val.shapePictureUrl && val.shapePictureUrl.length !== 0 ? (

                    <TouchableOpacity style={styles.shapeContainer}>

                      <Image style={styles.ImageStyle}
                        resizeMode='contain'
                        source={{ uri: `${val.shapePictureUrl}` }}
                      />
                      <View style={{ justifyContent: 'center' }}>
                        <Text styles={styles.nameOfShapeStyle}>{val.shapeName}</Text>
                      </View>
                    </TouchableOpacity>

                  ) : (<Text>No image</Text>)}

                </View>


              ))}
              <View style={styles.SkinColorStyle}>
                <Text style={styles.TextStyle2}>Select Your Skin Color</Text>
              </View>

              <View style={{ flex: 0.25, backgroundColor: 'white', borderRadius: 10, height: 0 }}>

                <View style={{ flex: 2, flexDirection: 'column' }}>
                  <View style={{ flex: 1, flexDirection: 'column' }}>
                    <View style={{ flex: 3, flexDirection: 'row', marginTop: 30, marginHorizontal: 10 }}>
                      <TouchableOpacity style={{
                        flex: 1, flexDirection: 'row', backgroundColor: '#ffe0bd',
                        height: 100, width: 100, borderRadius: 50, margin: 10
                      }} >
                      </TouchableOpacity>

                      <TouchableOpacity style={{
                        flex: 1, flexDirection: 'row', backgroundColor: '#eac086',
                        height: 100, width: 100, borderRadius: 50, margin: 10
                      }} >
                      </TouchableOpacity>


                      <TouchableOpacity style={{
                        flex: 1, flexDirection: 'row', backgroundColor: '#ffe39f',
                        height: 100, width: 100, borderRadius: 50, margin: 10
                      }} >
                      </TouchableOpacity>

                    </View>

                  </View>

                  <View style={{ flex: 1, flexDirection: 'column' }}>
                    <View style={{ flex: 3, flexDirection: 'row', marginHorizontal: 10, marginBottom: 30,marginTop:-270 }}>
                      <TouchableOpacity style={{
                        flex: 1, flexDirection: 'row', backgroundColor: '#2d170e',
                        height: 100, width: 100, borderRadius: 50, margin: 10
                      }} >
                      </TouchableOpacity>


                      <TouchableOpacity style={{
                        flex: 1, flexDirection: 'row', backgroundColor: '#6d4730',
                        height: 100, width: 100, borderRadius: 50, margin: 10
                      }} >
                      </TouchableOpacity>


                      <TouchableOpacity style={{
                        flex: 1, flexDirection: 'row', backgroundColor: '#cc9f88',
                        height: 100, width: 100, borderRadius: 50, margin: 10
                      }} >
                      </TouchableOpacity>

                    </View>

                  </View>


                </View>




              </View>

            </View>




          </View>


        </ImageBackground>
      </ScrollView>

    );
  }
}

const styles = StyleSheet.create({

  SkinColorStyleBox: {
    backgroundColor: 'white',
    borderRadius: 10,
    //height: 100,
    //marginTop: -500
    //flex: 1
  },
  SkinColorStyleText: {
    //backgroundColor: 'white',
    marginTop: 50,
    marginBottom: 20
  },
  SkinColorStyle: {

  },
  ImageBackgroundStyle: {
    width: '100%',
    marginTop: 0,
    height: 5500
  },
  TextStyle: {
    fontSize: 20,
    textAlign: 'center',
    marginTop: 90,
    color: 'white',
    fontWeight: 'bold'
  },
  TextStyle2: {
    fontSize: 20,
    textAlign: 'center',
    marginTop: 70,
    color: 'gray',
    fontWeight: 'bold'
  },
  Container: {
    backgroundColor: 'white',
    borderRadius: 10,
    marginLeft: 10,
    marginRight: 10,
    marginBottom: 10,
    marginTop: 50,
    height: 10,
    flex: 1
  },
  shapeContainer: {
    marginLeft: 10,
    marginRight: 10,
    width: '95%',
    marginTop: 10,


  },
  bottonClick: {
    width: 120,
    height: 300,
    backgroundColor: 'white',
    borderRadius: 10,
    borderWidth: 0.5,
    borderColor: '#E9E9E9',
    marginLeft: 20,
  },
  nameOfShape: {
    textAlign: 'center',
    marginBottom: 15,
    marginTop: 10,
    justifyContent: 'center'

  },
  nameOfShapeStyle: {
    color: 'gray',
    fontWeight: 'bold',
  },
  ImageStyle: {
    height: 300,
    width: '100%',
    justifyContent: 'center',

    borderWidth: 0.8,
    borderRadius: 40,
    borderColor: 'gray',
    marginTop: 10
  },

});
