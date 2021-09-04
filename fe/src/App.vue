<template>
  <div id="app">
    <div class="container-xl wrapper center">
      <div class="mb-3">
        <label class="form-label">Search for job by id:</label>
        <div class="row g-2">
          <div class="col">
            <input
              v-model="searchId"
              type="text"
              class="form-control"
              placeholder="Search for…"
            />
          </div>
          <div class="col-auto">
            <div
              v-if="!isloading"
              class="btn btn-white btn-icon"
              aria-label="Button"
              @click="searchForJob"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="icon icon-tabler icon-tabler-search"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                stroke-width="2"
                stroke="currentColor"
                fill="none"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                <circle cx="10" cy="10" r="7"></circle>
                <line x1="21" y1="21" x2="15" y2="15"></line>
              </svg>
            </div>
            <div
              v-if="isloading"
              class="btn btn-white btn-icon"
              aria-label="Button"
              @click="searchForJob"
            >
              <div
                class="spinner-border spinner-border-sm text-muted"
                role="status"
              ></div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="result != null" class="card">
        <div class="card-body">
          <h3 class="card-title">
            Advert {{ result.ad_number }} || applicants: {{ result.applicants }}
          </h3>
          <p>Biases</p>
          <ul id="example-1">
            <li v-for="biasKey in Object.keys(result.biases)" :key="biasKey">
              {{ biasKey}}: {{ result.biases[biasKey] }}
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      isloading: false,
      searchId: null,
      result: null,
    };
  },
  methods: {
    searchForJob() {
      const id = this.searchId;
      if (id.length > 300 || id.length < 1) {
        return null;
      }
      this.isloading = true;
      axios.get(`http://127.0.0.1:5000/jobs/${this.searchId}`).then((res) => {
        this.result = res.data;
      });
      this.isloading = false;
    },
  },
  name: "App",
};
</script>

<style>
.wrapper {
  margin-top: 10%;
}
</style>
