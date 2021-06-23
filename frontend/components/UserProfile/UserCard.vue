<template>
  <card class="card-user">
    <p class="card-text"></p>
    <div class="author">
      <div class="block block-one"></div>
      <div class="block block-two"></div>
      <div class="block block-three"></div>
      <div class="block block-four"></div>
      <a href="javascript:void(0)">
        <img class="avatar" src="img/emilyz.jpg" alt="..." />
        <h5 class="title">{{user.first_name}} {{user.second_name}}</h5>
      </a>
      <p class="description">TODO:!group!</p>
    </div>
    <p></p>
    <div class="card-description">
    TODO:!description!
    </div>
  </card>
</template>
<script>
export default {
  props:{
    user: Object
  }
};
</script>
<style></style>
