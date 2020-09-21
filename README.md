# United Kingdom COVID-19 alert level API (unofficial)

An API to expose the [COVID-19 alert level][alert-level-doc], as easily parseable JSON, for controlling lights and
klaxons and things.

GOV.UK does not expose this information in an easily-accessible format - there's no JSON endpoint or page on gov.uk
that can be readily scraped to obtain this information. The changes are reported with press releases that contain a
good set of keywords, so this project may be able to regularly scrape these. Until then, **this information is updated
on an ad-hoc basis by the project author (or contributors); do not rely on this API as a primary source of
information.**

[alert-level-doc]: https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/884352/slides_-_11_05_2020.pdf
