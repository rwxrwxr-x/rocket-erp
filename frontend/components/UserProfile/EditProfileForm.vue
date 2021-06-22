<template>
  <card>
    <h5 slot="header" class="title">Edit Profile</h5>
    <form @submit.prevent="updateProfile">
      <div class="row">
<!--        <div class="col-md-4">-->
<!--          <base-input-->
<!--            type="email"-->
<!--            label="Email"-->
<!--            :disabled="true"-->
<!--            placeholder="mike@email.com"-->
<!--            v-model="currentProfile.email"-->
<!--          >-->
<!--          </base-input>-->

<!--        </div>-->
      </div>

<!--      <div class="row">-->
<!--        <div class="col-md-6">-->
<!--          <base-input-->
<!--            type="text"-->
<!--            label="First Name"-->
<!--            placeholder="First Name"-->
<!--            v-model="currentProfile.first_name"-->
<!--          >-->
<!--          </base-input>-->
<!--        </div>-->
<!--        <div class="col-md-6">-->
<!--          <base-input-->
<!--            type="text"-->
<!--            label="Last Name"-->
<!--            placeholder="Last Name"-->
<!--            v-model="currentProfile.second_name"-->
<!--          >-->
<!--          </base-input>-->
<!--        </div>-->
<!--      </div>-->

<!--      <div class="row">-->
<!--        <div class="col-md-12">-->
<!--          <base-input label="About Me">-->
<!--            <textarea-->
<!--              class="form-control"-->
<!--              placeholder=""-->
<!--              v-model=""-->
<!--            >-->
<!--            </textarea>-->
<!--          </base-input>-->
<!--        </div>-->
<!--      </div>-->

      <base-button native-type="submit" type="primary" class="btn-fill">
        Save
      </base-button>
    </form>
  </card>
</template>
<script>

import { mapState } from 'vuex';

export default {

  methods: {
    updateProfile() {
      // alert('Your data: ' + JSON.stringify(this.user));
      // alert(JSON.stringify(this.$store.state))
      alert(JSON.stringify(this.$store.state) + 'ХУЙ')
    },
  }
};
</script>
<style></style>
