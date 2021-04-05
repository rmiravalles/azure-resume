# Azure Resume

Hi! :wave:

This is my resume hosted in Azure. I am following the guidelines described in the [A Cloud Guru Challenge](https://acloudguru.com/blog/engineering/cloudguruchallenge-your-resume-in-azure).

The deadline for this challenge is **May 31st**.

:star:[This is my resume](https://resume.rmiravalles.net/):star:

## Introduction

There are 7 steps to this challenge:

- [x] Create a GitHub repo.
- [x] Use HTML and CSS to build the website and store the code in the repo.
- [ ] Add a visitor count to the website.
- [x] Deploy the website to Azure Blob Storage.
- [x] Enable HTTPS and custom domain support.
- [x] Set up GitHub Actions.
- [ ] Write a blog post.

## My Progress

Here I'll describe my progress and what I did to achieve the outcomes of each step.

I had already started to experiment with this challenge before, when I first saw the original [Cloud Resume Challenge](https://cloudresumechallenge.dev/). Back then, I was just starting to learn Azure, and I wanted to try and adapt this challenge to Azure.

### The website

For the website, I used [this free template](https://startbootstrap.com/theme/resume), found on [Start Bootstrap](https://startbootstrap.com/).

### Storage Account

- Tutorial: [Host a static website on Blob Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website-host)

### Enable HTTPS and custom domain

- Quickstart: [Create an Azure CDN profile and endpoint](https://docs.microsoft.com/en-us/azure/cdn/cdn-create-new-endpoint)
- Tutorial: [Map a custom domain with HTTPS enabled](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-custom-domain-name?tabs=azure-portal#map-a-custom-domain-with-https-enabled)

### Set up GitHub Action

- Tutorial: [Use GitHub Actions to deploy your static website to Azure storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-static-site-github-actions)
- This workflow is compromised of 4 tasks:
  - [Checkout](https://github.com/actions/checkout): this will checkout our code, so the workflow can access it.
  - [Azure Login](https://github.com/marketplace/actions/azure-login): this will perform a login to Azure, so we can run commands. This is the `az login` command.
  - [Azure CLI](https://github.com/marketplace/actions/azure-cli-action): this allows us to automate our workflow by executing Azure CLI commands. We'll use this task twice; first to upload our content to the blob storage and after that to purge the CDN endpoint.
- I encountered an issue with the **Purge CDN endpoint** task.
- This is the command to run to purge the CDN endpoint: 
`az cdn endpoint purge --content-paths  "/*" --profile-name "CDN_PROFILE_NAME" --name "CDN_ENDPOINT" --resource-group "RESOURCE_GROUP"`
- The `--profile name` argument is the actual name of the CDN profile resource.
- The `--name` argument is the name of the endpoint, as it appears in the hostname *mywebsite.azureedge.net*.
- When you add an endpoint to your CDN profile, a new resource is created with a long name. This is not the name we should use for our command.

### The visitor counter

- [An easy to use visitor counter](https://hits.seeyoufarm.com/)
