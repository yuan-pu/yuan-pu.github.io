# Publication preview images

Every publication currently listed on the website has a preview filename reserved
below. Save each image here as a PNG using its exact filename. Images can be added
one at a time; papers without an image continue to display their venue badge.

| File                                | Paper                                                                  | Selected image                                           |
| ----------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------- |
| `medredflag.png`                    | MedRedFlag                                                             | Figure 1, upper portion shown in the supplied screenshot |
| `challenges-auditing.png`           | Challenges of Auditing                                                 | Figure 2                                                 |
| `antiplatelet.png`                  | Antiplatelet Resumption Timing (ADP)                                   | Figure 2                                                 |
| `counting-clues.png`                | Counting Clues                                                         | Figure 1                                                 |
| `egme.png`                          | Ethylene Glycol Monomethyl Ether (EGME)                                | Figure 1, panel shown in the supplied screenshot         |
| `glioblastoma.png`                  | Epigenetic Features and Gene Expression in Glioblastoma (PLOS CB 2025) | To be selected                                           |
| `gutgpt.png`                        | GutGPT Usability and Adoption (npj Digital Medicine 2025)              | To be selected                                           |
| `ml4h-roundtables.png`              | ML4H 2024 Research Roundtable Reflections (2025 preprint)              | To be selected                                           |
| `clinician-trust.png`               | Clinician Trust and Learning (DDW 2024)                                | To be selected                                           |
| `trajectory-flow-matching.png`      | Trajectory Flow Matching (NeurIPS 2024)                                | To be selected                                           |
| `human-algorithmic-interaction.png` | Human-Algorithmic Interaction (CHI 2024)                               | To be selected                                           |

The BibTeX entries already reference these filenames. Missing files fall back to
the venue badge. After the files are added, rebuild or publish the site to display
the images.

Keep the original image dimensions and aspect ratios. The website fits each image
inside a shared 4:3 area without cropping or stretching. Previews are decorative
and do not open or zoom when clicked. In the side-by-side layout, the image area
starts 0.75rem below the top of its row. No image shadows or rounded corners are added.

For a future publication, add `preview = {your-filename.png}` to its entry in
`_bibliography/papers.bib`, then save the corresponding image in this directory.
