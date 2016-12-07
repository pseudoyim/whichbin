# WhichBin?

## Motivation
  I recently ate at Whole Foods. As usual, I finished eating, got up to toss out my garbage, and then confronted this:

  <p align="center">
    <img src="https://cloud.githubusercontent.com/assets/9688260/20988965/975253da-bc98-11e6-8322-5b09f323f169.jpg" width="700"/>
  </p>

  This time, instead of having my typical mini-anxiety attack over where to toss out each of my pieces of garbage, I got an idea: What if my phone's camera could just tell me where each of these items should go?

  Sure, there are signs posted that are, in theory, supposed to tell me how to do this. But I don't have time to read. I already decided it's time to leave the store, and now I'm supposed to stand here and interpret a verbose chart listing what's recyclable/compostable/trashable/landfillable and what's not? No thanks. I want to help save the planet, but I got other locations on it to be at right now.

  Thesis: Less thinking; more blindly obeying my phone on how to sort my garbage.

  <p align="center">
    <img src="https://cloud.githubusercontent.com/assets/9688260/20988974/9cf1d090-bc98-11e6-8065-7be3780d1553.JPG" width="700"/>
  </p>

### Reward system
  Not only could the app identify the appropriate bin for your garbage items, but it could also keep track of how many objects you've correctly thrown away. This could be used to start an incentive program by which businesses could reward customers who contribute to the effort of properly sorting their garbage, thereby reducing the need for waste management facilities to correctly sort items downstream. It could also collect data on total waste disposed of in a given store and what kinds of waste predominate.

## Primary Python packages used
  - [OpenCV v3.1.0](http://opencv.org/opencv-3-1.html)
  - [Keras (TensorFlow backend)](https://keras.io/)
  - [Numpy](http://www.numpy.org/)

## Code
  Descriptions forthcoming.

## Performance
  None at this time. Still prototype.

## Future goals
  I currently have the image classification program running on my laptop. The near-term goal is to get this into a mobile app.
  I'm also working on assessing and improving the classification performance, which will likely require additions to training image dataset.
