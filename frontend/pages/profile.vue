<template>
  <div class="row">
    <div class="col-md-8"><edit-profile-form> </edit-profile-form></div>
    <div class="col-md-4"><user-card first_name="John" second_name="Shephard"> </user-card></div>
  </div>
</template>
<script>
import EditProfileForm from '../components/UserProfile/EditProfileForm.vue';
import UserCard from '../components/UserProfile/UserCard.vue';

export default {
  middleware: 'auth',
  name: 'user',

  components: {
    EditProfileForm,
    UserCard
  },
  created () {
    this.getProfile()
  },
  methods: {
    async getProfile() {
      await this.$store.dispatch('profile/me')
    }
  },

};
</script>
<style></style>
