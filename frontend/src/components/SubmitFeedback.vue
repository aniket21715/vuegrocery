<template>
  <NavBar />
  <div class="card mt-4 p-4">
    <h2 class="mb-3">Submit Feedback</h2>
    <form @submit.prevent="submitFeedback">
      <div class="mb-3">
        <label for="feedbackContent" class="form-label">Your Feedback:</label>
        <textarea v-model="feedbackContent" class="form-control" required></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit Feedback</button>
      <div v-if="successMessage" class="alert alert-success mt-3">
        {{ successMessage }}
      </div>
      <div v-if="errorMessage" class="alert alert-danger mt-3">
        {{ errorMessage }}
      </div>
    </form>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue';
export default {
  name: 'SubmitFeedback',
  components: {
    NavBar,
  },
  data() {
    return {
      feedbackContent: '',
      successMessage: '',
      errorMessage: '',
    };
  },
  methods: {
    async submitFeedback() {
      try {
        const accessToken = localStorage.getItem('access_token');

        const response = await fetch('https://vuegrocery.onrender.com/submit-feedback', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${accessToken}`,
          },
          body: JSON.stringify({
            content: this.feedbackContent,
          }),
        });

        if (response.ok) {
          this.successMessage = 'Feedback submitted successfully!';
          this.errorMessage = ''; // Clear any previous error message
          // Optionally, you can redirect the user or perform other actions here
        } else {
          const data = await response.json();
          this.errorMessage = data.error || 'Failed to submit feedback';
          this.successMessage = ''; // Clear any previous success message
        }
      } catch (error) {
        console.error('Error submitting feedback:', error);
        this.errorMessage = 'An error occurred while submitting feedback';
        this.successMessage = ''; // Clear any previous success message
      }
    },
  },
};
</script>

<style scoped>
/* Add your styling here */
.card {
  border: 2px solid #252a30;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(158, 138, 138, 0.1);
  padding: 20px;
}
</style>
