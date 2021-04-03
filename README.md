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
- [ ] Set up GitHub Actions.
- [ ] Write a blog post.

## My Progress

Here I'll describe my progress and what I did to achieve the outcomes of each step.

I had already started to experiment with this challenge before, when I first saw the original [Cloud Resume Challenge](https://cloudresumechallenge.dev/). Back then, I was just starting to learn Azure, and I wanted to try and adapt this challenge to Azure.

### The website

For the website, I used [this free template](https://startbootstrap.com/theme/resume), found on [Start Bootstrap](https://startbootstrap.com/).

### Storage Account

- Tutorial: [Host a static website on Blob Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website-host)
- From the Azure Portal, I created a new storage account.
- In the newly created storage account, under Settings, I clicked on the **Static website** option.

### Enable HTTPS and custom domain

- Quickstart: [Create an Azure CDN profile and endpoint](https://docs.microsoft.com/en-us/azure/cdn/cdn-create-new-endpoint)
- Tutorial: [Map a custom domain with HTTPS enabled](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-custom-domain-name?tabs=azure-portal#map-a-custom-domain-with-https-enabled)

### Set up GitHub Action

- [Use GitHub Actions to deploy your static website to Azure storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-static-site-github-actions)
